# weather/graphics/__init__.py

import weather.path
from weather.pbp import PoweredByPickles

DAY = 'DAY_ICON'
NIGHT = 'NIGHT_ICON'

TSV_FILE = weather.path.file_in_this_dir(__file__, 'icons.tsv')

class GraphicsDb(PoweredByPickles):
    def __init__(self):
        super().__init__('graphics', current_conditions_dict())
                
def current_conditions_dict():
    """Read NWS icon TSV file data into Python dict."""
    h, rows = _read_current_conditions_tsv()
    d = {r[0]: {k:v for k,v in zip(h[1:], r[1:])} for r in rows}
    return d

def _read_current_conditions_tsv():
    with open(TSV_FILE, 'r') as f:
        rows = [r for r in f.read().split('\n') if r.strip()]
        rows = [[c.strip('"') for c in r.split('\t')] for r in rows]
    return rows[0], rows[1:]

def get_nws_icon(fname):
    fp = weather.path.join('graphics', 'graphics_files', 'NWS',
                           '%s.b64' % fname)
    with open(fp, 'rb') as f:
        b = f.read()
    return b

def get_graphics_file(fname):
    fp = weather.path.join('graphics', 'graphics_files', '%s.b64' %\
                           fname)
    with open(fp, 'rb') as f:
        b = f.read()
    return b

weather_icons = GraphicsDb()
