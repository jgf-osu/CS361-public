import pickle
from . import path

class PoweredByPickles:
    """PoweredByPickles: The lazy dev's database™."""
    def __init__(self, fname):
        self._file = path.data_file('%s.pickle' % fname)
        self._data = dict()
        self._loaded = False

    @property
    def filepath(self):
        return self._file
        
    def _load(self):
        try:
            with open(self._file, 'rb') as f:
                self._data = pickle.load(f)
        except FileNotFoundError:
            pass
        finally:
            self._loaded = True

    def _save(self):
        with open(self._file, 'wb') as f:
            pickle.dump(self._data, f, pickle.HIGHEST_PROTOCOL)

    def __getitem__(self, key):
        if not self._loaded:
            self._load()
        return self._data[key]
    
    def __setitem__(self, key, value):
        if not self._loaded:
            self._load()
        self._data[key] = value
        self._save()

    def __contains__(self, key):
        if not self._loaded:
            self._load()
        return key in self._data

    def __iter__(self):
        if not self._loaded:
            self._load()
        return iter(self._data)
