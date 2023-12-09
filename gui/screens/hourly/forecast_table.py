# gui/screens/hourly/forecast_table.py

from gui import current
from gui.table import ForecastTable

class HourForecastTable(ForecastTable):
    def __init__(self, hourly_forecast):
        super().__init__(hourly_forecast)        
        self.number_of_columns = 3
        self._build_table_headers()

    def _build_table_headers(self):
        for i in range(self.number_of_columns):
            self._build_table_header(i)
        
    def _build_table_header(self, i):
        m = self.number_of_rows
        h0, h1 = self._forecast[i*m], self._forecast[i*m+m-1]
        txt = '%s (%s) – %s (%s)' % \
            (h0.abbr_date, h0.time, h1.abbr_date, h1.time)
        font = (self.font_family, self.font_size - 1, 'bold')
        header = self.gui_text(txt, font)
        self.table_headers.append([header])

    def get_elements(self, hourforecast):
        out = list()
        out.append(self.get_hourforecast_datetime(hourforecast))
        out.append(self.get_forecast_temperature(hourforecast))
        out.append(self.get_forecast_weather(hourforecast))
        return out

    def get_hourforecast_datetime(self, hourforecast):
        t_font = (self.font_family, self.font_size, 'bold')
        d = self.gui_text(hourforecast.abbr_date + ' ')
        t = self.gui_text(hourforecast.time, font=t_font)
        return [d, t]

def get_forecast():
    return current.forecast().hourly

def get_forecast_table():
    forecast = get_forecast()
    hft = HourForecastTable(forecast)
    return hft.table
