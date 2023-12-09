# gui/screens/settings/interface.py

import PySimpleGUI as sg
from weather import configurator as config
from weather.geocoder import Place, PlaceNotFound
from weather.geography import states

from .clear_cache import *

# DEBUG: when set to true, some useful debugging information will be
# printed to the the terminal during GUI operation
DEBUG = False

class SettingsInterface:
    def __init__(self):
        self._temperature_units_dict = dict()
        self._cfg = config.Configurator()       
        self._values = dict()
        self._window = self._get_window()

    # SettingsInterface: PUBLIC PROPERTIES
    @property
    def unsaved_changes(self):
        """Returns True if there are any unsaved changes. Otherwise,
        returns False."""
        return self._cfg.modified

    @property
    def valid_location(self):
        """Returns True if the current location can be
        geocoded. Otherwise, returns False."""
        try:
            p = Place(city=self._cfg['CITY'], state=self._cfg['STATE'])
            return True
        except PlaceNotFound:
            return False
       
    # SettingsInterface: PUBLIC METHODS
    def exit(self):
        """Returns True if there are no unsaved changes or if user
        confirms to exit without saving changes. Otherwise, returns
        False."""
        self.stage()
        if self.unsaved_changes:
            r = sg.popup_yes_no("Exit without saving changes?")
            if r == "Yes":
                self._cfg.revert()
            return r == "Yes"
        else:
            return True

    def read(self):
        self._event, self._values = self._window.read()
        self.debug('read()')
        if 'Cache' in self._event:
            do_cache_action(self._event)
        return self._event

    def close(self):
        self._window.close()

    def save(self):
        """Called when the user clicks a "Save" button."""
        self.stage()
        if self.valid_location or not self.unsaved_changes:
            self._save_settings()
        else:
            self._ask_to_revert()

    def stage(self):
        """Stages updates to app configuration, but does not commit
        changes."""
        self._stage_temperature()
        self._stage_text_field('-CITY-', 'CITY')
        self._stage_text_field('-STATE-', 'STATE')
        self.debug('after stage()')

    def debug(self, msg):
        """Print some useful debug info if we're in DEBUG mode."""
        if not DEBUG:
            return
        print(msg)
        print('READ: %s' % str(self._values))
        print('CFGR: %s' % str(self._cfg.settings))
        print('CFG.modified:', self._cfg.modified,
              self._cfg.modification_count)
        print()

    # SettingsInterface: PRIVATE PROPERTIES
    @property
    def _layout(self):
        """Returns main layout of the Settings screen."""
        layout = list()
        layout.append([self._temperature_units_input,
                       clear_cache_frame()])
        layout.append([self._location_input])
        layout.append([self._main_buttons])
        return layout
    
    @property
    def _location_input(self):
        """Returns a PySimpleGui Frame elemeent that contains labels
        and input fields for the City setting and the State
        setting."""        
        city = self._city_input
        state = self._state_input
        return sg.Frame('Forecast Location', [city+state])

    @property
    def _city_input(self):
        """Returns label and input field for the City setting."""
        city = self._cfg['CITY']
        city_label = sg.Text('City:')
        city_input = sg.Input(city, key='-CITY-')
        return list([city_label, city_input])

    @property
    def _state_input(self):
        """Returns label and input field for the State setting."""
        state_label = sg.Text('State:')
        state_input = self._state_dropdown_menu
        return list([state_label, state_input])

    @property
    def _state_dropdown_menu(self):
        state = self._cfg['STATE']
        key = '-STATE-'
        return sg.Combo(states, key=key, default_value=state,
                        size=(10,10), readonly=True)

    @property
    def _temperature_units_input(self):
        """Returns PySimpleGUI Frame element that contains
        radiobuttons to select temperature Units setting."""
        radbtns = list()
        radbtns.append(self._radiobutton_units_f)
        radbtns.append(self._radiobutton_units_c)
        radbtns.append(self._radiobutton_units_fc)
        return sg.Frame('Temperature Units', radbtns)

    @property
    def _radiobutton_units_f(self):
        label = 'Fahrenheit'
        cfg_val = 'F'
        sg_key = '-UNITS (F)-'        
        return self._radiobutton_units(label, cfg_val, sg_key)

    @property
    def _radiobutton_units_c(self):
        label = 'Celsius'
        cfg_val = 'C'
        sg_key = '-UNITS (C)-'        
        return self._radiobutton_units(label, cfg_val, sg_key)

    @property
    def _radiobutton_units_fc(self):
        label='Fahrenheit & Celsius'
        cfg_val = 'FC'
        sg_key = '-UNITS (BOTH)-'
        return self._radiobutton_units(label, cfg_val, sg_key)

    @property
    def _main_buttons(self):
        """Returns a row (list) of command buttons for the Settings
        screen."""
        row = list()
        row.append(self._save_button)
        row.append(self._home_button)
        row.append(self._save_and_home_button)
        return row

    @property
    def _save_button(self):
        label = 'Save & Keep Editing'
        tt = 'Save changes to settings.'
        key = '-[BTN] SAVE-'
        return sg.Button(label, key=key, tooltip=tt)

    @property
    def _home_button(self):
        label = 'Go Home'
        tt = 'Return to the home screen.'
        key = '-[BTN] HOME-'
        return sg.Button(label, key=key, tooltip=tt)

    @property
    def _save_and_home_button(self):
        label = 'Save & Go Home'
        tt = 'Save settings and go to home screen.'
        key='-[BTN] SAVE&HOME-'
        return sg.Button(label, key=key, tooltip=tt)
    
    # SettingsInterface: PRIVATE METHODS
    def _get_window(self):
        window = sg.Window('Weather > Settings', self._layout,
                           enable_close_attempted_event=True)
        return window

    def _radiobutton_units(self, label, cfg_val, sg_key):
        """Builds and returns a sg.Radio GUI element for temperature
        selection UI."""
        self._temperature_units_dict[sg_key] = cfg_val
        selected = self._cfg['UNITS'] == cfg_val
        rb = sg.Radio(label, 'UNITS', default=selected, key=sg_key)
        return [rb]

    def _stage_text_field(self, sg_key, cfg_key):
        """Stages a Configurator change from GUI update."""
        if self._values[sg_key]:
            self._cfg[cfg_key] = self._values[sg_key]
        
    def _stage_temperature(self):
        """Stage an update to config file if a different temperature
        unit has been selected."""
        for sg_key, cfg_val in self._temperature_units_dict.items():
            if self._values[sg_key]:
                self._cfg['UNITS'] = cfg_val
   
    def _save_settings(self):
        """Save to config file and report result."""
        result = self._cfg.save()
        if result == config.SUCCESS:
            sg.popup("Settings updated.")
        elif result == config.NOT_MODIFIED:
            sg.popup("No changes to save.")
        self.debug('after save()')

    def _ask_to_revert(self):
        """Ask user to revert invalid location."""
        msg = "The location %s, %s, was not found. Revert to "\
            "original value of %s, %s?"
        vals = (self._cfg['CITY'], self._cfg['STATE'], 
                self._cfg.original_value('CITY'),
                self._cfg.original_value('STATE'))
        r = sg.popup_yes_no(msg % vals)
        if r == "Yes":
            self._do_revert()
        else:
            self._confirm_save()

    def _do_revert(self):
        """Revert to previous location."""
        self._revert_text_field('-CITY-', 'CITY')
        self._revert_text_field('-STATE-', 'STATE')
        self.debug('after _do_revert()')

    def _revert_text_field(self, sg_key, cfg_key):
        """Revert Configurator value and update GUI."""
        self._cfg.revert(cfg_key)
        self._values[sg_key] = self._cfg[cfg_key]
        self._window.fill({sg_key: self._cfg[cfg_key]})
        
    def _confirm_save(self):
        """Ask user to confirm saving an invalid location."""
        msg = "Really save unknown location %s, %s?" %\
            (self._cfg['CITY'], self._cfg['STATE'])
        r = sg.popup_yes_no(msg)
        if r == "Yes":
            self._save_settings()

