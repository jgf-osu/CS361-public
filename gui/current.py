# gui/current.py

from weather import configurator as config
from weather.geocoder import Place, PlaceNotFound
from weather.station import find_nearest_station
from weather.graphics import DAY, weather_icons, get_nws_icon
from weather.forecast import get_forecast_for_point

class WeatherReport:
    def __init__(self):
        try:
            station_ = station()
            self._cc = station_.current_conditions
        except PlaceNotFound:
            self._cc = None
            
    @property
    def temperature(self):
        """Returns a string. String contains temperature data if it is
        available. If no such data is available, the string will
        describe the problem."""
        try:
            t = self._build_temperature_str()
        except KeyError:
            t = 'Temperature not reported.'
        return t

    @property
    def weather(self):
        """Returns a string. String contains weather conditions data
        if it is available. If no such data is available, the string
        will describe the problem."""
        if 'weather' in self._cc:
            return self._cc['weather']
        return 'No conditions reported.'
        
    @property
    def report(self):
        """Returns a string. String contains temperature data and
        weather conditions data if such data are available. If any
        data is unavailable, the string will describe the problem."""
        if self._cc is None:
            return 'Location unknown; no weather report.'
        else:
            return self.temperature + ' ' + self.weather

    def _build_temperature_str(self):
        """Builds a string from current conditions dict without
        checking to see if key exists in dictionary."""
        if units() == 'F':
            return self._cc['temp_f'] + '℉'
        if units() == 'C':
            return self._cc['temp_c'] + '℃'
        else:
            t = self._cc['temperature_string']
            return t.replace('F', '℉').replace('C', '℃')


class WeatherIcon:
    def __init__(self, conditions_dict):
        self._cc = conditions_dict

    @property
    def weather_str(self):
        """Returns None if there is no reported weather
        conditions. Otherwise, returns a string containing the
        reported weather conditions."""
        if self._cc is None:
            return None
        elif 'weather' not in self._cc:
            return None
        else:
            return self._cc['weather']

    @property
    def nws_icon_exists(self):
        """Returns True if there is a NWS weather icon for reported
        conditions. Otherwise returns False."""
        if self.weather_str is None:
            return False
        else:
            return self.weather_str in weather_icons
    
    @property
    def filename(self):
        """Returns a string containing the file name of the icon based
        on reported conditions."""
        if self._cc is None:
            return 'void'
        elif self.nws_icon_exists:
            return weather_icons[self.weather_str][DAY]
        else:
            return 'earth'

    @property
    def tooltip(self):
        """Returns a string for use as an icon tooltip."""
        if self._cc is None:
            return 'No weather data received.'
        elif self.weather_str is None:
            return 'No weather conditions reported by station %s.'\
                % self._cc['station_id']
        elif self.nws_icon_exists:
            return self.weather_str
        else:
            return 'No specific icon found for "%s" conditions.'\
                % self.weather_str

    @property
    def data(self):
        """Returns Base64-encoded icon data."""
        return get_nws_icon(self.filename)
            
    
def city_and_state():
    """Returns a tuple of two strings '(CITY, STATE)' populated by the
    location currently configured by the user."""
    cfg = config.Configurator()
    return cfg['CITY'], cfg['STATE']

def place():
    """Returns a Place object representing the geographical location
    currently configured by the user."""
    city, state = city_and_state()
    return Place(city=city, state=state)

def place_not_found():
    """Returns True if the location currently configured by the user
    cannot be properly geocoded. Otherwise, returns False."""
    try:
        p = place()
        return False
    except PlaceNotFound:
        return True

def station():
    """Returns a Station object representing the weather station
    nearest to the location currently configured by the user."""
    return find_nearest_station(place())

def units():
    """Returns the currently chosen temperature units: F/C/BOTH."""
    cfg = config.Configurator()
    return cfg['UNITS']

def conditions():
    """Returns a dictionary object containing the most recent
    observation at the weather station nearest to the location
    currently configured by the user. If the location configured by
    the user cannot be geocoded, returns None."""
    if place_not_found():
        return None
    else:
        return station().current_conditions

def coordinates_str():
    """Returns a string depicting lat/lon coordinates of location
    currently configured by the user. If a problem is encountered in
    geocoding the user location, the string will contain information
    about that problem."""
    try:
        location = place()
        return '%.4f, %.4f' % (location.lat, location.lon)
    except PlaceNotFound:
        return 'We were unable to find coordinates.'

def location_str():
    """Returns a string in the format 'CITY, STATE' based on the
    location currently configured by the user."""
    return '%s, %s' % city_and_state()

def weather():
    """Returns a string containing the latest weather report from the
    station nearest to the location currently configured by the
    user. If a problem is encountered in generating the report, the
    string will contain information about that problem."""
    w = WeatherReport()
    return w.report

def icon():
    """Returns a WeatherIcon instance based on current weather
    conditions as provided by the conditions() function."""
    cc = conditions()
    return WeatherIcon(cc)

def forecast():
    try:
        return get_forecast_for_point(place())
    except PlaceNotFound:
        return None
