# gui/screens/home/layout.py

import PySimpleGUI as sg
from gui import current
from .encryptor import encryptor_button

def get_window():
    window = sg.Window('Weather', _get_layout(), finalize=True)
    if '-WEATHER STATION-' in window.AllKeysDict:
        window['-WEATHER STATION-'].set_cursor('hand2')
    return window 

def _get_layout():
    cols = list()
    cols.append(_current_conditions_column())
    cols.append(_navigation_column())
    return [cols]

def _current_conditions_column():
    rows = list()
    rows.append(_current_conditions_heading())
    rows.append([_weather_icon_column(),
                 _weather_report_column()])
    rows.append(_last_observation())
    return sg.Column(rows)

def _navigation_column():
    rows = list()
    rows.append(_hourly_forecast_button())
    rows.append(_daily_forecast_button())
    rows.append(encryptor_button())
    rows.append(_settings_button())
    return sg.Column(rows)

def _weather_icon_column():
    ico = current.icon()
    img = sg.Image(ico.data, tooltip=ico.tooltip)
    return sg.Column([[img]])

def _current_conditions_heading():
    font = ('sans', 12, 'bold underline')
    return _text_row('CURRENT CONDITIONS', font)

def _current_location_text():
    font = ('sans', 14, 'bold')
    return _text_row(current.location_str(), font)

def _current_coordinates_text():
    font = ('sans',8)
    return _text_row(current.coordinates_str(), font)

def _current_weather_text():
    font = ('sans', 10)
    return _text_row(current.weather(), font)

def _weather_report_column():
    rows = list()
    rows.append(_current_location_text())
    rows.append(_current_coordinates_text())
    rows.append(_current_weather_text())
    col = sg.Column(rows, vertical_alignment='top')
    return col

def _station_not_contacted_text():
    font = ('sans', 8)
    return _text_row('Station not contacted.', font)

def _click_for_more_station_data_text():
    cc = current.conditions()
    tt = "Click to open web browser and see data from last two "\
        "days at station %s." % cc['station_id']
    font = ('sans', 8)
    key = '-WEATHER STATION-'
    return _text_row(cc['observation_time'], font, key=key,
                    enable_events=True, tooltip=tt)

def _last_observation():
    if current.conditions() is None:
        return _station_not_contacted_text()
    else:
        return _click_for_more_station_data_text()

def _hourly_forecast_button():
    key = '-[BTN] HOURLY-'
    tt = "See the hourly forecast for the next 24 hours."
    btn = sg.Button('Hourly Forecast', key=key, tooltip=tt)
    return [btn]

def _daily_forecast_button():
    key = '-[BTN] DAILY-'
    tt = "See the 10-day forecast."
    btn = sg.Button('Daily Forecast', key=key, tooltip=tt)
    return [btn]

def _settings_button():
    key = '-[BTN] SETTINGS-'
    tt = "Change temperature units or forecast location."
    btn = sg.Button('Settings', key=key, tooltip=tt)
    return [btn]

def _text_row(txt, font, **kwargs):
    t = sg.Text(txt, font=font, **kwargs)
    return [t]
