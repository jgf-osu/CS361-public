import time
import os.path

ONE_DAY = 60 * 60 * 24
ONE_HOUR = 60 * 60

def get_timely_resource(fpath, create_func, get_func, stale=ONE_DAY):
    try:
        # if file exists, make sure it's not stale
        mtime = os.path.getmtime(fpath)
        ctime = time.mktime(time.localtime())
        if ctime - mtime > stale:
            # file is stale, so create a new copy
            create_func()
    except OSError:
        # file doesn't exist, so create it
        create_func()
    return get_func()
