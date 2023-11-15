from xml.etree.ElementTree import parse as xml_parse
from . import path
from .timer import get_timely_resource, ONE_HOUR
from .downloader import download_resource
from .geography import Point, haversine_distance

STATION_INDEX_URL = 'https://w1.weather.gov/xml/current_obs/index.xml'
STATION_INDEX_XML = path.data_file('stations.xml')

#
##
### XML HANDLING
def _parse_xml(fpath):
    with open(fpath, 'r') as f:
        document = xml_parse(f)
    return document

def _xml_to_dict(node):
    out = dict()
    for child in node:
        out[child.tag] = child.text
    return out

#
##
### HANDLING THE STATION INDEX
def _parse_station_index():
    return _parse_xml(STATION_INDEX_XML)

def _download_station_index():
    """Download a new station index file from NWS."""
    download_resource(STATION_INDEX_URL, STATION_INDEX_XML)

def get_station_index():
    """Return station index as a parsed XML file. If file is stale,
    download a new one before parsing."""
    return get_timely_resource(STATION_INDEX_XML, _download_station_index,
                               _parse_station_index)

def find_nearest_station(home_point):
    """Takes a Point object. Finds the nearest weather station."""
    document = get_station_index()
    nearest_station = None
    shortest_distance = None
    
    # find the station nearest to home and its haversine distance from
    # home
    for station in document.iter('station'):
        station = Station(_xml_to_dict(station))
        distance = haversine_distance(home_point, station)
        if nearest_station is None or distance < shortest_distance:
            nearest_station = station
            shortest_distance = distance
    return nearest_station

#
##
### CLASS DEFINITIONS
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
            download_resource(self._data['xml_url'], self._file)
        return downloader

    def _parser(self):
        def parser():
            return _parse_xml(self._file)
        return parser

