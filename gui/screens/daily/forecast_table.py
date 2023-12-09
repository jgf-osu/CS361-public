# gui/screens/daily/forecast_table.py

import PySimpleGUI as sg
from gui import current
from gui.table import ForecastTable

from debug import debug as debug_
def debug(text, **kwargs):
    text = '<gui/screens/daily/forecast_table.py> ' + text
    debug_(text, **kwargs)

class DayForecastTable(ForecastTable):
    def __init__(self, daily_forecast):
        super().__init__(daily_forecast)
        self.number_of_columns = 1

    def get_elements(self, dayforecast):
        out = list()
        out.append(self.get_dayforecast_day(dayforecast))
        out.append(self.get_dayforecast_date(dayforecast))
        out.append(self.get_forecast_temperature(dayforecast))
        out.append(self.get_forecast_weather(dayforecast))
        return out

    def get_dayforecast_day(self, dayforecast):
        return [self.gui_text(dayforecast.day)]

    def get_dayforecast_date(self, dayforecast):
        return [self.gui_text(dayforecast.date)]

def get_forecast():
    debug("Getting forecast.")
    return current.forecast().daily

def get_forecast_table():
    debug("Getting forecast to build table.")
    forecast = get_forecast()
    debug("Got forecast. Building table.")
    dft = DayForecastTable(forecast)
    return dft.table
