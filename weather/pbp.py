# weather/pbp.py

import pickle
import os
from . import path

class PoweredByPickles:
    """PoweredByPickles: The lazy dev's database™."""
    def __init__(self, fname, data_dict=None):
        self._file = path.data_file('%s.pickle' % fname)
        if data_dict is None:
            self._data = dict()
        else:
            assert(isinstance(data_dict, dict))
            self._data = data_dict
            self._save()
        self._loaded = False

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

    def __str__(self):
        if not self._loaded:
            self._load()
        return str(self._data)

    def __repr__(self):
        return "%s('%s', data_dict=%s)" %\
            (__class__.__name__, self.filepath, self._data)

    def __len__(self):
        return len(self._data)
        
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


def destroy_pickle(pbp_obj):
    """Deletes the archive of a PoweredByPickles object. If the
    archive does not exist, this does nothing."""
    if not isinstance(pbp_obj, PoweredByPickles):
        raise TypeError
    try:
        os.remove(pbp_obj.filepath)
    except FileNotFoundError:
        pass
