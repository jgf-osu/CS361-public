# weather/geocoder.py

import json
from .geography import Point
from . import path
from .timer import ApiGovernor, ONE_SECOND
from .pbp import PoweredByPickles

# Geocoding service API
#   (Documentation: https://geocode.maps.co/)
GEOCODE_SERVICE = 'https://geocode.maps.co/search'
GeocodeApi = ApiGovernor(GEOCODE_SERVICE, time_between_hits=2*ONE_SECOND)

class KnownPlaces(PoweredByPickles):
    def __init__(self, fname='known_places'):
        super().__init__(fname)

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("Place already known.")
        else:
            super().__setitem__(key, value)


class Place(Point):
    def __init__(self, dbname='known_places', **kwargs):
        self._build_request(**kwargs)
        self._db = KnownPlaces(dbname)
        self._load_response()        
        lat, lon = self._coordinates
        super().__init__(lat, lon)

    def __getitem__(self, key):
        try:
            return self._result[key]
        except KeyError as e:
            print("Could not find key %s." % key)
            print(self._result)
            raise e

    def __str__(self):
        return '%s (%f, %f)' % (self.name, self.lat, self.lon)
        
    @property
    def name(self):
        return self._result['display_name']

    @property
    def key(self):
        return json.dumps(self._request, sort_keys=True)

    @property
    def _errmsg_place_not_found(self):
        return "Could not find %s." % str(self._request)

    @property
    def _coordinates(self):
        return self._response['lat'], self._response['lon']
    
    def _load_response(self):
        if not self.key in self._db:
            self._send_api_request()
        self._response = self._db[self.key]
        if self._response is PlaceNotFound:
            raise PlaceNotFound(self._errmsg_place_not_found)
        
    def _build_request(self, **kwargs):
        """Return request data validated against API specs."""
        data = {'country': 'US'}
        valid = {'street', 'city', 'state', 'postalcode'}
        for k, v in kwargs.items():
            if k in valid:
                data[k] = v
            else:
                raise KeyError("Invalid parameter: %s" % k)
        self._request = data

    def _send_api_request(self):
        r = GeocodeApi.get(GEOCODE_SERVICE, params=self._request)
        if not r.json():
            result = PlaceNotFound
        else:
            result = r.json()[0]
        self._db[self.key] = result


class PlaceNotFound(Exception):
    pass
