# weather/forecast.py

import requests
from datetime import datetime
from weather import timer
from weather.pbp import PoweredByPickles
from weather.geography import Point


from debug import debug as debug_
def debug(text, **kwargs):
    text = '<weather/forecast.py> ' + text
    debug_(text, **kwargs)

    
# NOAA National Weather Service API
#   Documentation:
#   https://www.weather.gov/documentation/services-web-api
NWS_API_POINT_URL = 'https://api.weather.gov/points/'
NwsApi = timer.ApiGovernor(NWS_API_POINT_URL)


class ForecastStore(PoweredByPickles):
    """Store forecasts, indexed by Points."""
    def __init__(self, fname='forecast_store'):
        super().__init__(fname)

    def __setitem__(self, key, value):
        raise NotImplementedError("Use the ForecastStore.add method.")
    
    def __getitem__(self, point):
        assert(isinstance(point, Point))
        key = point_to_forecast_key(point)
        return super().__getitem__(key)

    def __contains__(self, point):
        assert(isinstance(point, Point))
        key = point_to_forecast_key(point)
        return super().__contains__(key)

    def add(self, point):
        assert(isinstance(point, Point))
        debug("Store adding <%s>." %\
              point_to_forecast_key(point))
        if point in self:
            raise ForecastError("Point already exists in store.")
        self._save_forecast(Forecast(point, self))
        return self.__getitem__(point)

    def retrieve(self, point):
        assert(isinstance(point, Point))
        if point in self:
            debug("Store retrieving <%s>." %\
                  point_to_forecast_key(point))
            return self[point]
        else:
            return self.add(point)

    def update(self, forecast):
        assert(isinstance(forecast, Forecast))
        debug("Store updating <%s>." % forecast.key)
        self._save_forecast(forecast)

    def _save_forecast(self, forecast):
        assert(isinstance(forecast, Forecast))
        super().__setitem__(forecast.key, forecast)


class Forecast:
    def __init__(self, point, store):
        self._store = store
        self._point = point

        if point in store:
            self = store[point]
        else:
            self._items = dict()

    def __getitem__(self, key):
        debug("Getting resource <%s> from: %s" %\
              (key, str(self.stored_items)))
        if key not in self or self._items[key].stale:
            if key not in self:
                debug("Resource <%s> not found." % key)
            else:
                debug("Resource <%s> is stale." % key)
            self._items[key] = self._download_data(key)
            debug("Downloaded resource <%s>. %s" %\
                  (key, self._items[key].report))
            self.update()
        else:
            debug("Resource is NOT stale. %s" % self._items[key].report)
        return self._items[key]

    def __contains__(self, key):
        return key in self._items

    def __iter__(self):
        return iter(self._items)

    @property
    def point(self):
        return self._point
    
    @property
    def daily(self):
        """Returns a list of daily forecasts."""
        return self._get_daily_forecast()

    @property
    def hourly(self):
        """Returns a list of hourly forecasts."""
        return self._get_hourly_forecast(24)

    @property
    def hourly_forecast_url(self):
        return self._get_item_url_from_index('hourly')

    @property
    def daily_forecast_url(self):
        return self._get_item_url_from_index('daily')

    @property
    def forecast_index_url(self):
        return NWS_API_POINT_URL + self.key
     
    @property
    def key(self):
        return point_to_forecast_key(self.point)

    @property
    def stored_items(self):
        return self._items.keys()

    def update(self):
        self._store.update(self)

    @property
    def _path_to_hourly_url(self):
        return ['index', 'properties', 'forecastHourly']

    @property
    def _path_to_daily_url(self):
        return ['index', 'properties', 'forecast']

    @property
    def _path_to_daily_forecast_data(self):
        return ['daily', 'properties', 'periods']

    @property
    def _path_to_hourly_forecast_data(self):
        return ['hourly', 'properties', 'periods']

    def _get_daily_forecast(self):
        path = self._path_to_daily_forecast_data
        url = self.daily_forecast_url
        df = lambda f: DayForecast(f, url)
        return [df(f) for f in _follow_path(self, path, url)]
    
    def _get_hourly_forecast(self, limit):
        path = self._path_to_hourly_forecast_data
        url = self.hourly_forecast_url
        out = list()
        for i, forecast in enumerate(_follow_path(self, path, url)):
            if i == limit: break
            out.append(HourForecast(forecast, url))
        return out
    
    def _get_item_url(self, key):
        if key == 'index':
            return self.forecast_index_url
        else:
            return self._get_item_url_from_index(key)

    def _get_item_url_from_index(self, key):
        if key == 'hourly':
            path = self._path_to_hourly_url
        elif key == 'daily':
            path = self._path_to_daily_url
        else:
            raise ForecastError("Unkown forecast item: %s." % key)
        return _follow_path(self, path, self.forecast_index_url)

    def _download_data(self, key):
        debug("Downloading <%s> from API." % key)
        url = self._get_item_url(key)
        r = NwsApi.get(url)
        r = r.json()
        return ForecastItemData(r)


class ForecastItemData(timer.TimelyObject, dict):
    def __init__(self, forecast_data):
        timer.TimelyObject.__init__(self, timer.ONE_HOUR)
        dict.__init__(self, {k:v for k,v in forecast_data.items()})


class ApiDataWrapper:
    def __init__(self, api_data, url):
        self._data = api_data
        self._url = url

    def __getitem__(self, key):
        return self._data[key]

    def __str__(self):
        return str(self._data)

    def follow(self, path):
        return _follow_path(self, path, self.url)

    @property
    def url(self):
        return self._url


class BasicForecast(ApiDataWrapper):
    def __init__(self, api_data, url):
        super().__init__(api_data, url)

    @property
    def abbr_date(self):
        return self.start_time.strftime('%m/%d/%y')

    @property
    def start_time(self):
        path = ['startTime']
        timestamp = self.follow(path)
        return ForecastTimestamp(timestamp)

    @property
    def end_time(self):
        path = ['endTime']
        timestamp = self.follow(path)
        return ForecastTimestamp(timestamp)
        
    @property
    def temp_f(self):
        path = ['temperature']
        return str(self.follow(path))

    @property
    def temp_c(self):
        return _temp_c_str(self.temp_f)

    @property
    def weather(self):
        path = ['shortForecast']
        return self.follow(path)


class DayForecast(BasicForecast):
    def __init__(self, api_data, url):
        super().__init__(api_data, url)

    @property
    def day(self):
        path = ['name']
        return self.follow(path)

    @property
    def date(self):
        return self.abbr_date


class HourForecast(BasicForecast):
    def __init__(self, api_data, url):
        super().__init__(api_data, url)

    @property
    def time(self):
        return self.start_time.time

    @property
    def datetime(self):
        date = self.start_time.date
        time = self.time
        return '%s, at %s' % (date, time)


class ForecastTimestamp:
    def __init__(self, iso_8601_timestamp):
        self._timestamp = iso_8601_timestamp
        self._datetime = datetime.fromisoformat(self._timestamp)

    @property
    def day_of_week(self):
        return self.strftime('%A')

    @property
    def month(self):
        return self.strftime('%B')

    @property
    def year(self):
        return self.strftime('%Y')

    @property
    def time(self):
        return self.strftime('%I:%M %p')

    @property
    def day_of_month(self):
        return str(int(self.strftime('%d')))

    @property
    def date(self):
        date = [self.month, self.day_of_month + ',', self.year]
        return ' '.join(date)

    def strftime(self, fstr):
        return self._datetime.strftime(fstr)


class ForecastError(Exception):
    pass


def raise_from_malformed_data(path, url, key):
    msg = "Data is malformed when trying to follow this path:\n" +\
        "   %s\n" % str(path) +\
        "Key '%s' not found. " % key +\
        "Check API results at:\n" +\
        "   %s\n" % url
    raise ForecastError(msg)
        
def point_to_forecast_key(point):
    return '%.4f,%.4f' % (point.lat, point.lon)

def forecast_key_to_point(key):
    lat, lon = [float(_) for _ in key.split(',')]
    return Point(lat, lon)

def get_forecast_for_point(point):
    fs = ForecastStore()
    return fs.retrieve(point)

def _temp_c_str(temp_f_str):
    f = float(temp_f_str)
    c = (f - 32) * (5/9)
    return '%.1f' % c

def _follow_path(root, path, debug_url):
    dest = root
    for i, step in enumerate(path):
        try:
            dest = dest[step]
        except KeyError:
            raise_from_malformed_data(path, debug_url, step)
    return dest

