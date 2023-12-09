# gui/screens/home/__init__.py

import PySimpleGUI as sg
import webbrowser

from gui import current
from gui.screens import settings
from gui.screens import daily
from gui.screens import hourly

from .layout import get_window
from .encryptor import do_encryptor

def show():
    window = get_window()
    event = _ui_loop(window)
    window.close()
    if event:
        _navigate(event)

def browse_to_station():
    url = current.conditions()['two_day_history_url']
    webbrowser.open(url)

def _navigate(event):
    if 'SETTINGS' in event:
        settings.show()
    elif 'HOURLY' in event:
        hourly.show()
    elif 'DAILY' in event:
        daily.show()

def _handle_event(event):
    if event == '-WEATHER STATION-':
        browse_to_station()
    elif event == '-ENCRYPTOR-':
        do_encryptor()
        
def _ui_loop(window):
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            return False
        if '[BTN]' in event:
            return event
        else:
            _handle_event(event)

