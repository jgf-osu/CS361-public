# gui/__init__.py

from weather import defaults
from . import screens
        
def run():
    defaults.save()
    screens.home.show()
