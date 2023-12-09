# weather/geography.py

import math

class Point:
    """A geographical point with latitude and longitude."""
    def __init__(self, lat, lon):
        self._lat = float(lat)
        self._lon = float(lon)

    def __repr__(self):
        return 'Point(%f, %f)' % self.lat, self.lon

    def __str__(self):
        return self.__repr__()

    @property
    def lat(self):
        return self._lat

    @property
    def lon(self):
        return self._lon


def haversine_distance(point0, point1):    
    """Returns distance in meters between two lat/lon coordinate
    points."""
    # Based on: http://www.movable-type.co.uk/scripts/latlong.html
    R = 6371*10**3
    phi0 = point0.lat * math.pi/180
    phi1 = point1.lat * math.pi/180
    delta_phi = (point1.lat-point0.lat) * math.pi/180
    delta_lambda = (point1.lon-point0.lon) * math.pi/180

    a = math.sin(delta_phi/2)**2 +\
        math.cos(phi0) * math.cos(phi1) *\
        math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL",
          "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME",
          "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH",
          "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
          "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI",
          "WY"]
