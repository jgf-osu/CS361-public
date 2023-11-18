import time
import os.path

ONE_SECOND = 1
ONE_HOUR = ONE_SECOND  * 60
ONE_DAY = ONE_HOUR * 24
ONE_WEEK = ONE_DAY * 7

class TimelyObject:
    def __init__(self, obj, lifespan):
        self._obj = obj
        self._last_update = current_time()
        self._lifespan = lifespan

    @property
    def stale(self):
        if current_time() - self._last_update > self._lifespan:
            return True
        return False

    def __setitem__(self, key, value):
        self._obj[key] = value

    def __getitem__(self, key):
        return self._obj[key]

    def __iter__(self):
        return iter(self._obj)

    def __contains__(self, key):
        return key in self._obj

    def __str__(self):
        return str(self._obj)


def current_time():
    return time.mktime(time.localtime())

def get_timely_resource(fpath, create_func, get_func, stale=ONE_DAY):
    try:
        # if file exists, make sure it's not stale
        mtime = os.path.getmtime(fpath)
        ctime = current_time()
        if ctime - mtime > stale:
            # file is stale, so create a new copy
            create_func()
    except OSError:
        # file doesn't exist, so create it
        create_func()
    return get_func()
