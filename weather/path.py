# weather/path.py

import os.path

PACKAGE_PATH = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = 'data'
DATA_PATH = os.path.join(PACKAGE_PATH, DATA_DIR)

def join(*args):
    args = tuple([PACKAGE_PATH] + list(args))
    return os.path.join(*args)

def data_file(*args):
    args = tuple([PACKAGE_PATH, DATA_DIR] + list(args))
    return os.path.join(*args)

def list_data_files():
    """Returns a list of absolute filepaths to files in the data
    directory."""
    return [data_file(f) for f in list_data_filenames()]

def list_data_filenames():
    out = list()
    for fname in os.listdir(DATA_PATH):
        if fname[0] == '.': continue
        fpath = data_file(fname)
        if os.path.isfile(fpath):
            out.append(fname)
    return out

def file_in_this_dir(script_file, fname):
    """Pass __file__ variable and a filename to get an absolute path
    to filename in the calling script's directory."""
    dir_path = os.path.dirname(os.path.realpath(script_file))
    fpath = os.path.join(dir_path, fname)
    return fpath
