import socket
import json
import sys
from . import configurator as config
from .geocoder import Place, PlaceNotFound
from .station import find_nearest_station

def encode(python_dict):
    j = json.dumps(python_dict)
    return j.encode('utf-8')

def decode(bytes_arr):
    s = bytes_arr.decode('utf-8')
    return json.loads(s)

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
        self._write('Listening on port: %i\n' % self._cfg['PORT'])
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:            
            s.bind((self._cfg['HOST'], self._cfg['PORT']))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                self._write('Connected by ' + str(addr) + '\n')
                while True:
                    bytes_arr = conn.recv(1024)
                    if not bytes_arr: break
                    req = decode(bytes_arr)
                    try:
                        location = Place(city=req['city'], state=req['state'])
                        weather_station = find_nearest_station(location)
                        rstatus = 'ok'
                        rmsg = weather_station.brief_report
                    except PlaceNotFound:
                        rstatus = 'PlaceNotFound'
                        rmsg = 'Unable to retrieve weather report. Could not geocode the provided location. Please try a different location.'
                    except UnicodeEncodeError:
                        rstatus = 'UnicodeEncodeError'
                        rmsg = 'Unable to retrieve weather report. A remote resource was improperly formatted. Please try again later.'
                    except Exception:
                        rstatus = 'UnknownError'
                        rmsg = 'An unknown error ocurred.'
                        
                    response = {
                        'status' : rstatus,
                        'response-type': 'current-conditions',
                        'message': rmsg
                    }
                    payload = encode(response)
                    conn.sendall(payload)
