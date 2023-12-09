# gui/screens/hourly/layout.py

import PySimpleGUI as sg
from gui import current
from .forecast_table import get_forecast, get_forecast_table

def get_window():
    title = 'Weather > Hourly Forecast'
    layout = _get_layout()
    return sg.Window(title, layout)

def _get_layout():
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
    font = ('sans', 12, 'bold italic')
    text = sg.Text('HOURLY FORECAST', font=font)
    return [text]

def _description():
    forecast = get_forecast()
    font = ('sans', 8, 'bold')
    txt = 'Hourly forecasts for the next 24 hours. From %s to %s.' %\
        (forecast[0].datetime, forecast[-1].datetime)
    text = sg.Text(txt, font=font)
    return [text]

def _location():
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
