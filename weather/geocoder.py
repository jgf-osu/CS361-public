import requests
import json
from .geography import Point
from . import path
from .pbp import PoweredByPickles

GEOCODE_SERVICE = 'https://geocode.maps.co/search'

class KnownPlaces(PoweredByPickles):
    def __init__(self):
        super().__init__('known_places')

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError("Place already known.")
        else:
            super().__setitem__(key, value)


class Place(Point):
    def __init__(self, street=None, city=None, state=None,
                 postalcode=None):
        data = {'country': 'US'}
        if street is not None:
            data['street'] = street
        if city is not None:
            data['city'] = city
        if state is not None:
            data['state'] = state
        if postalcode is not None:
            data['postalcode'] = postalcode

        self._request = json.dumps(data, sort_keys=True)

        seen = KnownPlaces()
        if self._request in seen:
            self._result = seen[self._request]            
        else:                    
            # REQUEST GEOCODING
            r = requests.get(GEOCODE_SERVICE, params=data)
            r.raise_for_status()
            if not r.json():
                raise PlaceNotFound("Could not find %s, %s." % (city, state))
            self._result = r.json()[0]
            seen[self._request] = self._result

        lat, lon = self._result['lat'], self._result['lon']
        super().__init__(lat, lon)

    @property
    def name(self):
        return self._json['display_name']
        
    def __getitem__(self, key):
        return self._json[key]


class PlaceNotFound(Exception):
    pass
