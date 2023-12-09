# gui/screens/daily/__init__.py

import PySimpleGUI as sg
from gui import current
from gui.screens import home
from debug import debug
from .layout import get_window

from debug import debug as debug_
def debug(text, **kwargs):
    text = '<gui/screens/daily/__init__.py> ' + text
    debug_(text, **kwargs)

def show():
    if current.place_not_found():
        sg.popup("No daily forecast. Location cannot be found.")
        home.show()
    else:
        _show()

def _show():
    debug("Getting window.")
    window = get_window()
    event = _ui_loop(window)
    window.close()
    if event:
        _navigate(event)
        
def _ui_loop(window):
    debug("Got window.")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            return False
        if event == '-[BTN] HOME-':
            return event

def _navigate(event):
    if 'HOME' in event:
        home.show()
