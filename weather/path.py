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
