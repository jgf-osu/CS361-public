# weather/timer.py

import time
import requests
import os.path
from .pbp import PoweredByPickles

ONE_SECOND = 1
ONE_MINUTE = ONE_SECOND  * 60
ONE_HOUR = ONE_MINUTE * 60
ONE_DAY = ONE_HOUR * 24
ONE_WEEK = ONE_DAY * 7

MAX_TRIES = 5

class ApiGovernor:
    """A class for regulating the rate of requests sent to an API."""
    def __init__(self, api_url, time_between_hits=ONE_SECOND):
        self._url = api_url
        self._last_hit = 0
        self._rate = time_between_hits
        self._tries = 0

    @property
    def url(self):
        return self._url

    @property
    def last_request(self):
        """Return timestamp of last request sent."""
        return self._last_hit

    def wait_if_needed(self):
        while seconds_since(self._last_hit) < self._rate:
            wait_a_sec()

    def get(self, url, **kwargs):
        self.wait_if_needed()
        self._last_hit = current_time()
        try:
            return self._get_fn(url, **kwargs)
        except requests.exceptions.HTTPError as e:
            if self._tries < MAX_TRIES:
                return self.get(url, **kwargs)
            else:
                raise e

    def _get_fn(self, url, **kwargs):
        # separated from get() for sake of being able to do unit
        # testing without hitting an actual web API
        self._tries += 1
        r = requests.get(url, **kwargs)
        r.raise_for_status()
        self._tries = 0
        return r


class TimelyObject:
    """An object that can go stale."""
    def __init__(self, lifespan):
        self._last_update = current_time()
        self._lifespan = lifespan

    @property
    def stale(self):
        if current_time() - self._last_update > self._lifespan:
            return True
        return False

    @property
    def lifespan(self):
        return self._lifespan

    @property
    def time_left(self):
        return self.lifespan - (current_time() - self._last_update)

    @property
    def report(self):
        return "Lifespan: %i; Time Left: %i" %\
            (self.lifespan, self.time_left)


def current_time():
    """Returns the current time in number seconds since the epoch."""
    return int(time.mktime(time.localtime()))

def seconds_since(timestamp):
    return current_time() - timestamp

def get_timely_resource(fpath, create_func, get_func, stale=ONE_DAY):
    """Retrieve a file that might be stale. If it is stale or does not
    exist, use create_func to create a new version of it. Returns the
    results of a call to get_func."""
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

def wait_a_sec():
    """Pause execution for one second."""
    time.sleep(ONE_SECOND)
