from .pbp import PoweredByPickles

# CONFIGURATOR 'SAVE' FLAGS
SUCCESS = 1
NOT_MODIFIED = 2

class Setting:
    def __init__(self, value = None):
        self._staged = False
        self._original_value = value
        self._value = value

    @property
    def staged(self):
        return self._staged
        
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self._value = new_value
        self._staged = True

    @property
    def original_value(self):
        return self._original_value

    def commit(self):
        self._original_value = self._value
        self._staged = False

    def revert(self):
        self._value = self._original_value        
        self._staged = False
        
        
class Configurator(PoweredByPickles):
    def __init__(self, fname='configuration'):
        self._modified = 0
        self._staged = {}
        self._fname = fname
        
        super().__init__(fname)        
        for key in super().__iter__():
            current_value = super().__getitem__(key)
            self._staged[key] = Setting(current_value)

    @property
    def modified(self):
        return self._modified > 0

    @property
    def staged(self):
        return self._staged

    def __setitem__(self, key, value):
        if key not in self._staged:            
            self._staged[key] = Setting(value)
        else:
            if self._staged[key].value == value:
                return NOT_MODIFIED
            self._staged[key].value = value
        self._modified += 1
        return SUCCESS

    def __getitem__(self, key):
        return self._staged[key].value

    def __iter__(self):
        return iter(self._staged)

    def __contains__(self, key):
        return key in self._staged

    def revert(self, key=None):
        if key is not None:
            self._staged[key].revert()
            self._modified -= 1
        else:
            for key in self._staged:
                self.revert(key)

    def original_value(self, key):
        return self._staged[key].original_value

    def reload(self):
        self = self.__init__(self._fname)

    def staged(self, key):
        return self._staged[key].staged

    def save(self):
        if not self.modified:
            return NOT_MODIFIED
        else:
            for key in self._staged:
                new_key = not super().__contains__(key)
                changes_staged = self._staged[key].staged
                if new_key or changes_staged:
                    new_value = self._staged[key].value
                    super().__setitem__(key, new_value)
                    self._staged[key].commit()
        self._modified = 0
        return SUCCESS

    
class DefaultSetter(Configurator):
    def __init__(self, fname=None):
        if fname is None:
            super().__init__()
        else:
            super().__init__(fname)

    def __setitem__(self, key, value):
        """Only add if it's not already there."""
        try:
            tmp = super().__getitem__(key)
        except KeyError:
            super().__setitem__(key, value)
