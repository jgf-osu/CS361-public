# weather/service.py

import socket
import json
import sys
from . import configurator as config
from .geocoder import Place, PlaceNotFound
from .station import find_nearest_station

class WeatherServiceRequest:
    def __init__(self, bytes_arr):
        self._data = decode(bytes_arr)

    @property
    def city(self):
        return self._data['city']

    @property
    def state(self):
        return self._data['state']


class WeatherServiceResponse:
    def __init__(self, request):
        self._req = request

    @property
    def _response(self):
        resp = {'response-type': 'current-conditions'}
        try:
            resp['status'] = 'ok'
            resp['msg'] = self._weather_report
        except PlaceNotFound:
            resp['status'] = 'PlaceNotFound'
            resp['msg'] = 'Could not find that place.'
        except Exception as e:
            resp['status'] = e.__class__.__name__
            resp['msg'] = str(e)
        return resp

    @property
    def _weather_report(self):
        location = Place(city=self._req.city, state=self._req.state)
        weather_station = find_nearest_station(location)
        return weather_station.brief_report

    @property
    def data(self):
        return encode(self._response)


class WeatherService:
    def __init__(self, host=None, port=None):
        self._cfg = config.Configurator()
        if host is not None:
            self._cfg['HOST'] = host
        if port is not None:
            self._cfg['PORT'] = port
        if host is not None or port is not None:
            self._cfg.save()
            
    @property
    def name(self):
        return 'WEATHER SERVICE'

    @property
    def host(self):
        return self._cfg['HOST']

    @property
    def port(self):
        return self._cfg['PORT']

    def _write(self, txt):
        out = '[%s] ' % self.name + txt
        sys.stderr.write(out)
    
    def listen(self):
        self._write('Listening on port: %i\n' % self.port)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:            
            s.bind((self.host, self.port))
            s.listen(1)
            self._conn, self._addr = s.accept()
            self._handle_connection()
            
    def _handle_connection(self):
        with self._conn:
            self._write('Connected by ' + str(self._addr) + '\n')
            while True:
                bytes_arr = self._conn.recv(1024)
                if not bytes_arr: break
                request = WeatherServiceRequest(bytes_arr)
                response = WeatherServiceResponse(request)
                self._conn.sendall(response.data)


def encode(python_dict):
    j = json.dumps(python_dict)
    return j.encode('utf-8')

def decode(bytes_arr):
    s = bytes_arr.decode('utf-8')
    return json.loads(s)

