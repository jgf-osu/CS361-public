# gui/screens/daily/layout.py

import PySimpleGUI as sg
from gui import current
from .forecast_table import get_forecast, get_forecast_table


from debug import debug as debug_
def debug(text, **kwargs):
    text = '<gui/screens/daily/layout.py> ' + text
    debug_(text, **kwargs)

    
def get_window():
    title = 'Weather > Daily Forecast'
    layout = _get_layout()
    return sg.Window(title, layout)

def _get_layout():
    debug("Getting layout.")
    main = []
    main.append(_heading())
    main.append(_location())
    main.append([sg.HorizontalSeparator()])
    main.append(_description())
    main.append([sg.HorizontalSeparator()])
    main.append(get_forecast_table())
    main.append(_home_button())
    return main

def _heading():
    debug("Getting heading.")
    font = ('sans', 12, 'bold italic')
    text = sg.Text('DAILY FORECAST', font=font)
    return [text]

def _description():
    debug("Getting description.")
    forecast = get_forecast()
    font = ('sans', 8, 'bold')
    txt = 'Daily forecasts available from %s to %s.' %\
        (forecast[0].date, forecast[-1].date)
    text = sg.Text(txt, font=font)
    return [text]

def _location():
    debug("Getting location.")
    return _location_col() + _coordinate_col()

def _location_col():
    font = ('sans', 14)
    text = sg.Text(current.location_str(), font=font)
    return [text]

def _coordinate_col():
    font = ('sans', 8)
    pad = (0,0),(7,0)
    text = sg.Text(current.coordinates_str(), font=font, pad=pad)
    return [text]

def _home_button():
    label = 'Go Home'
    tt = 'Return to the home screen.'
    key = '-[BTN] HOME-'
    btn = sg.Button(label, key=key, tooltip=tt)
    return [sg.Push(), btn, sg.Push()]
