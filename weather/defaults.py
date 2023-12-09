# weather/defaults.py
from .configurator import Configurator

class DefaultSetter(Configurator):
    def __init__(self, fname=None):
        if fname is None:
            super().__init__()
        else:
            super().__init__(fname)

    def __setitem__(self, key, value):
        """Only add if it's not already there."""
        try:
            tmp = super().__getitem__(key)
        except KeyError:
            super().__setitem__(key, value)

def save():
    cfg = DefaultSetter()
    cfg['UNITS'] = 'F'
    cfg['CITY'] = 'Cleveland'
    cfg['STATE'] = 'OH'
    cfg.save()
