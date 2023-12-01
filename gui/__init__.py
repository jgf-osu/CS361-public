import PySimpleGUI as sg
import webbrowser
from weather import configurator as config
from weather import path
from weather.geography import states
from weather.geocoder import Place, PlaceNotFound
from weather.station import find_nearest_station
from weather.graphics import icon_from_cc

# NAVIGATION BUTTONS
SHOW_HOME = '-BTN-HOME-'
SHOW_SETTINGS = '-BTN-SETTINGS-'

# SETTINGS SCREEN
UNITS_CELSIUS = '-UNITS-C-'
UNITS_FAHRENHEIT = '-UNITS-F-'
UNITS_BOTH = '-UNITS-BOTH-'
SAVE_SETTINGS = '-SAVE-SETTINGS-'
SAVE_AND_HOME ='-SAVE AND GO HOME-'

# HOME SCREEN
WEATHER_STATION = '-WEATHER-STATION-'

class GUI:
    def __init__(self):
        self._cfg = config.Configurator()
        self._main_window = None

    def run(self):
        self._show_home()

    def _show_home(self):
        location_str = '%s, %s' % (self._cfg['CITY'], self._cfg['STATE'])
        coordstr = 'Unknown coordinates.'
        try:
            location = Place(city=self._cfg['CITY'], state=self._cfg['STATE'])
            coordstr = '%.4f, %.4f' % (location.lat, location.lon)
            weather_station = find_nearest_station(location)
            weather = weather_station.current_conditions
        except:
            weather = None
            sg.popup("Warning: could not find location %s" % location_str)    

        # CURRENT CONDITIONS COLUMN
        icon, icon_tooltip = icon_from_cc(weather)

        self.weather_report = self._cc_report(weather)        
        col0 = [
            [sg.Text('CURRENT CONDITIONS', font=('sans', 12, 'bold underline'))],
            [
                sg.Column([
                    [sg.Image(icon, tooltip=icon_tooltip)]
                ]),
                sg.Column([
                    [sg.Text(location_str, font=('sans', 14, 'bold'))], # city, state
                    [sg.Text(coordstr, font=('sans',8))], # lat, lon
                    [sg.Text(self.weather_report, font=('sans', 10))] # temp & weather
                ], vertical_alignment='top')
            ],
            [self._cc_obs_time(weather)]
        ]

        # MAIN NAVIGATION COLUMN
        col1 = [
            [sg.Button('Encrypted Report', key='-BTN-ENCRYPT-',
                       tooltip="Show an encrypted weather report.")],
            [sg.Button('Settings', key='-BTN-SETTINGS-',
                       tooltip="Change temperature units or forecast location.")]
        ]  

        layout = [[sg.Column(col0), sg.Column(col1)]]
        self._main_window = sg.Window('Weather', layout, finalize=True)
        if WEATHER_STATION in self._main_window.AllKeysDict:
            self._main_window[WEATHER_STATION].set_cursor('hand1')

        while True:
            event, values = self._main_window.read()
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break
            if event == '-BTN-SETTINGS-':
                self._main_window.close()
                self._show_settings()
            if event == '-BTN-ENCRYPT-':
                sg.popup('Encrypted Weather', demsar(self.weather_report))
            if event == WEATHER_STATION:
                webbrowser.open(weather['two_day_history_url'])

        self._main_window.close()

    def _forecast_location(self):
        return Place(city=self._cfg['CITY'], state=self._cfg['STATE'])

    def _update_cfg(self, values):       
        if values[UNITS_CELSIUS]: self._cfg['UNITS'] = 'C'
        if values[UNITS_FAHRENHEIT]: self._cfg['UNITS'] = 'F'
        if values[UNITS_BOTH]: self._cfg['UNITS'] = 'FC'
        self._cfg['CITY'] = values['-CITY-']
        self._cfg['STATE'] = values['-STATE-']

    def _settings_layout(self):
        # SETTINGS SCREEN: LOCATION
        city_label = sg.Text('City:')
        city_input = sg.InputText(self._cfg['CITY'], key='-CITY-')
        city = [city_label, city_input]
        state_label = sg.Text('State:')    
        state_input = sg.Combo(states, key='-STATE-',
                               default_value=self._cfg['STATE'], size=(10,10),
                               readonly=True)
        state = [state_label, state_input]
        location = sg.Frame('Forecast Location', [city + state])

        # SETTINGS SCREEN: TEMPERATURE UNITS
        radiobtn_fahrenheit = sg.Radio(
            'Fahrenheit', 'UNITS', default=self._cfg['UNITS'] == 'F',
            key=UNITS_FAHRENHEIT)

        radiobtn_celsius = sg.Radio(
            'Celsius', 'UNITS', default=self._cfg['UNITS'] == 'C',
            key=UNITS_CELSIUS)

        radiobtn_fc = sg.Radio(
            'Fahrenheit & Celsius', 'UNITS',
            default=self._cfg['UNITS'] == 'FC', key=UNITS_BOTH)
        
        temp_units = sg.Frame('Temperature Units', [
            [radiobtn_fahrenheit], [radiobtn_celsius], [radiobtn_fc]
        ])

        # SETTINGS SCREEN: BUTTONS
        tt = 'Save changes to settings.'
        SaveButton = sg.Button('Save & Keep Editing', tooltip=tt, key=SAVE_SETTINGS)
        tt = 'Return to the home screen.'
        HomeButton = sg.Button('Go Home', tooltip=tt, key=SHOW_HOME)
        tt = 'Save settings and go to home screen.'
        SaveAndHome = sg.Button('Save & Go Home', tooltip=tt, key=SAVE_AND_HOME)

        # SETTINGS SCREEN: LAYOUT
        layout = [[temp_units], [location], [SaveButton, HomeButton, SaveAndHome]]
        return layout

    def _save_settings(self):
        result = self._cfg.save()
        if result == config.SUCCESS:
            sg.popup("Settings updated.")
        elif result == config.NOT_MODIFIED:
            sg.popup("No changes to save.")

    def _settings_btn_save(self, event, values):
        self._update_cfg(values)
        try:
            if self._cfg.staged('CITY') or self._cfg.staged('STATE'):        
                # if user-provided "City, State" is an unknown
                # location, this will throw a PlaceNotFound error:
                self._forecast_location()
            self._save_settings()
        except PlaceNotFound:
            msg = "The location %s, %s, was not found. Revert to "\
                "original value of %s, %s?"
            orig = (self._cfg['CITY'], self._cfg['STATE'], 
                    self._cfg.original_value('CITY'),
                    self._cfg.original_value('STATE'))
            r = sg.popup_yes_no(msg % orig)
            if r == "Yes":
                self._cfg.revert('CITY')
                self._cfg.revert('STATE')
                self._main_window.close()
                self._main_window = sg.Window('Weather > Settings',
                                   self._settings_layout())
            else:
                msg = "Really save unkown location %s, %s?" %\
                    (self._cfg['CITY'], self._cfg['STATE'])
                r = sg.popup_yes_no(msg)
                if r == "Yes":
                    self._save_settings()

    def _settings_btn_home(self, event, values):
        self._update_cfg(values)
        if self._cfg.modified:
            r = sg.popup_yes_no("Exit without saving changes?")
            if r == "Yes":
                self._cfg.revert()
            return r == "No"
        else:
            return False
            
    def _show_settings(self):    
        # SETTINGS SCREEN LOOP
        self._main_window = sg.Window('Weather > Settings', self._settings_layout())
        go = True
        while go:
            event, values = self._main_window.read()
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break
            if event == SAVE_SETTINGS:
                self._settings_btn_save(event, values)               
            if event == SHOW_HOME:
                go = self._settings_btn_home(event, values)
            if event == SAVE_AND_HOME:
                self._settings_btn_save(event, values)
                go = self._settings_btn_home(event, values)

        self._cfg.reload()
        self._main_window.close()
        self._show_home()
    
    def _cc_obs_time(self, cc):
        """Takes a Station.current_conditions object. Returns string of
        text telling when the last observation was made."""
        font = ('sans', 8)
        if cc is None:
            return sg.Text('Station not contacted.', font=font)
        else:
            tt = "Click to open web browser and see data from last two days"\
                " at station %s." % cc['station_id']
            obs = sg.Text(cc['observation_time'], font=font,
                          enable_events=True, key=WEATHER_STATION,
                          tooltip=tt)
            return obs

    def _cc_report(self, cc):
        """Takes a Station.current_conditions object. Returns string of
        text telling the weather."""
        font = ('sans', 10)
        df, dc = '℉', '℃'        
        if cc is None:
            return sg.Text('Weather unkown.')
        else:
            if self._cfg['UNITS'] == 'F':
                temp_key, unit_str = 'temp_f', '℉'
                report = cc[temp_key] + unit_str
            elif self._cfg['UNITS'] == 'C':
                temp_key, unit_str = 'temp_c', '℃'
                report = cc[temp_key] + unit_str
            else:
                temp_key = 'temperature_string'
                report = cc[temp_key].replace('F', df).replace('C', dc)
            if 'weather' in cc:
                report = report + ' ' + cc['weather']
            return report

import json
import socket
        
def encode(python_obj):
    j = json.dumps(python_obj)
    return j.encode('utf-8')

def decode(bytes_arr):
    s = bytes_arr.decode('utf-8')
    return json.loads(s)
        
def demsar(msg):
    req = encode(msg)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 12345))
        s.sendall(req)
        response = decode(s.recv(1024))
    return response
        
def run():
    g = GUI()
    g.run()
