# gui/table.py

import PySimpleGUI as sg
from gui import current

class Table:
    def __init__(self, data, parser_fn=None):
        if parser_fn is None:
            self._data = data
        else:
            self._data = parser_fn(data)

    @property
    def font_size(self):
        return self._default('_font_size', 8)
    @font_size.setter
    def font_size(self, size):
        self._font_size = size

    @property
    def font_family(self):
        return self._default('_font_family', 'sans')
    @font_family.setter
    def font_family(self, font_family):
        self._font_family = font_family

    @property
    def default_font(self):
        return (self.font_family, self.font_size)

    @property
    def number_of_columns(self):
        return self._default('_number_of_columns', 4)
    @number_of_columns.setter
    def number_of_columns(self, i):
        self._number_of_columns = i

    @property
    def number_of_rows(self):
        """Number of rows of data in the table. Does not include
        header rows."""
        x = len(self._data)
        y = self.number_of_columns
        return x//y

    @property
    def data_width(self):
        return len(self._data[0])

    @property
    def table_headers(self):
        return self._default('_table_headers', list())

    @property
    def table(self):
        cols = [list() for i in range(self.number_of_columns)]
        for i, col in enumerate(cols):
            if self.table_headers:
                col.append(self.table_headers[i])
            col.append(self._data_column(i))
        return [sg.Column(c) for c in cols]

    def gui_text(self, text, font=None):
        if font is None:
            font = self.default_font        
        return sg.Text(text, font=font)

    def _data_column(self, i):
        col = [list() for j in range(self.data_width)]
        m, n = self.number_of_rows, self.number_of_columns
        for x in range(i*m, i*m+m):
            for y, element in enumerate(self._data[x]):
                col[y].append(element)
        return [sg.Column(z) for z in col]

    def _default(self, attr, value):
        if not hasattr(self, attr):
            setattr(self, attr, value)
        return getattr(self, attr)


class ForecastTable(Table):
    def __init__(self, forecast_data):
        self._forecast = forecast_data
        super().__init__(forecast_data, self._forecast_parser)

    def _forecast_parser(self, forecast_data):
        return [self.get_elements(f) for f in forecast_data]

    def get_elements(self, basicforecast):
        raise NotImplementedError

    def get_forecast_temperature(self, basicforecast):
        units = current.units()
        f = basicforecast.temp_f + '℉'
        c = basicforecast.temp_c + '℃'
        if units == 'F' or units == 'C':
            temp = (f, c)[units == 'C']
        elif units == 'FC':
            temp = '%s (%s)' % (f, c)
        else:
            raise Exception("Bad configuration: 'UNITS' = %s" % temp)
        return [self.gui_text(temp)]

    def get_forecast_weather(self, basicforecast):
        return [self.gui_text(basicforecast.weather)]
