# weather/configurator.py

from .pbp import PoweredByPickles

# CONFIGURATOR FLAGS
SUCCESS = 1
NOT_MODIFIED = 2
NO_VALUE = None

class Setting:
    def __init__(self, existing_value=NO_VALUE):
        self._value = existing_value
        self._saved_value = existing_value     
        self._staged = False

    @property
    def staged(self):
        """Returns True if the setting has a staged update. Otherwise,
        returns False."""
        return self._staged
        
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        if new_value != self._value:
            self._value = new_value
            self._staged = True

    @property
    def saved_value(self):
        return self._saved_value

    def commit(self):
        """If the Setting has a staged update, this will save the
        staged value. Returns the saved value."""        
        self._saved_value = self._value
        self._staged = False
        return self._saved_value

    def revert(self):
        """If the Setting has a staged update, this will unstage
        it. Otherwise, does nothing."""
        self._value = self._saved_value        
        self._staged = False
        
        
class Configurator(PoweredByPickles):
    def __init__(self, fname='configuration'):
        self._modified = 0
        self._staged = dict()
        self._fname = fname
        self._set_item_result = 0
        
        super().__init__(fname)       
        for key in super().__iter__():
            current_value = super().__getitem__(key)            
            self._staged[key] = Setting(current_value)

    def __setitem__(self, key, value):
        """Stages the value of a setting. If the setting is not
        currently in the config file, this will stage its addition to
        the config file with the value provided. If the staged change
        would result in a modification of the config file, the value
        of Configurator.result will be set to the SUCCESS flag;
        otherwise, Configurator.result will be set to the NOT_MODIFIED
        flag."""
        new_key = key not in self._staged
        if not new_key and self._staged[key].value == value:
            self._set_item_result = NOT_MODIFIED
        else:
            if not new_key:
                self._staged[key].value = value
            else:
                self._staged[key] = Setting()
                self._staged[key].value = value                
            self._modified += 1
            self._set_item_result = SUCCESS

    def __getitem__(self, key):
        return self._staged[key].value

    def __iter__(self):
        return iter(self._staged)

    def __contains__(self, key):
        return key in self._staged
            
    @property
    def modified(self):
        """Returns True if any modifications to the config file have
        been staged. Otherwise, returns False."""
        return self._modified > 0

    @property
    def modification_count(self):
        """Returns the number of staged changes."""
        return self._modified

    @property
    def result(self):
        """Returns a flag set by the last setitem operation."""
        return self._set_item_result

    @property
    def settings(self):
        """Returns a dictionary showing staged changes."""
        d = {k: s.value for k, s in self._staged.items()}
        return d
    
    def revert(self, key=None):
        """If a key is provided, unstage a change to the setting at
        that key. If no key is provided, unstage all changes to all
        settings. If a setting is new, reverting it will remove it
        entirely from the record of staged changes."""
        if key is None:
            for key in self._staged:
                self.revert(key)
        elif self._staged[key].staged:
            self._staged[key].revert()
            if self._staged[key].value is NO_VALUE:
                del self._staged[key]
            self._modified -= 1
                
    def original_value(self, key):
        """Returns the original value of the key."""
        return self._staged[key].saved_value

    def reload(self):
        """Reloads the Configurator, based on the current state of its
        config file."""
        self = self.__init__(self._fname)

    def staged(self, key):
        """Returns True if the setting has a change staged. Otherwise,
        returns False."""
        return self._staged[key].staged

    def save(self):
        """Saves staged changes to the config file. If this operation
        succeeds, it returns the SUCCESS flag. If no changes were made
        to the config file, it returns the NOT_MODIFIED flag."""
        if not self.modified:
            return NOT_MODIFIED
        else:
            for key in self._staged:
                if self._staged[key].staged:
                    new_value = self._staged[key].commit()
                    super().__setitem__(key, new_value)                    
                    self._modified -= 1
        return SUCCESS

    def _setting_is_new(self, key):
        """Returns True if the setting is not currently found in the
        configuration file. Otherwise, returns False."""
        return not super().__contains__(key)

