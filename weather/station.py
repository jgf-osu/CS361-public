# weather/station.py

import requests
from xml.etree.ElementTree import parse as xml_parse
from . import path
from .timer import get_timely_resource, ONE_HOUR
from .geography import Point, haversine_distance

STATION_INDEX_URL = 'https://w1.weather.gov/xml/current_obs/index.xml'
STATION_INDEX_XML = path.data_file('stations.xml')

class Station(Point):
    def __init__(self, xml_data):
        self._data = xml_data
        self._file = path.data_file('%s.xml' % xml_data['station_id']) 
        lat, lon = xml_data['latitude'], xml_data['longitude']
        super().__init__(lat, lon)
        
    @property
    def id(self):
        return self._data['station_id']

    @property
    def name(self):
        return self._data['station_name']

    @property
    def url(self):
        return self._data['xml_url']

    @property
    def current_conditions(self):
        document = get_timely_resource(self._file, self._downloader(),
                                       self._parser(), stale=ONE_HOUR)
        current_observation = document.getroot()
        return _xml_to_dict(current_observation)

    @property
    def brief_report(self):
        report = ''
        
        if 'temperature_string' in self.current_conditions:
            temp = self.current_conditions['temperature_string']
            df, dc = '℉', '℃'
            report += temp.replace('F', df).replace('C', dc)

        if 'weather' in self.current_conditions:
            report += ' ' + self.current_conditions['weather']
        
        if not report:
            report = "No report available for this location."

        return report

    def _downloader(self):
        def downloader():
            _download_resource(self.url, self._file)
        return downloader

    def _parser(self):
        def parser():
            return _parse_xml(self._file)
        return parser


def get_station_index():
    """Return station index as a parsed XML file. If file is stale,
    download a new one before parsing."""
    return get_timely_resource(STATION_INDEX_XML, _download_station_index,
                               _parse_station_index)

def find_nearest_station(point):
    """Takes a Point object. Returns a Station object representing the
    weather station nearest to the Point."""
    document = get_station_index()
    nearest_station, shortest_distance = None, None
    for station in document.iter('station'):
        station = Station(_xml_to_dict(station))
        distance = haversine_distance(point, station)
        if nearest_station is None or distance < shortest_distance:
            nearest_station, shortest_distance = station, distance
    return nearest_station

def _download_resource(remote, local):
    r = requests.get(remote)
    r.raise_for_status()
    with open(local, 'w', encoding='utf-8') as f:
        f.write(r.text)

def _parse_xml(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        document = xml_parse(f)
    return document

def _xml_to_dict(node):
    out = dict()
    for child in node:
        out[child.tag] = child.text
    return out

def _parse_station_index():
    return _parse_xml(STATION_INDEX_XML)

def _download_station_index():
    _download_resource(STATION_INDEX_URL, STATION_INDEX_XML)
