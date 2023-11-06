from weather.gui import GUI
from weather.configurator import DefaultSetter

if __name__ == '__main__':
    defaults = DefaultSetter()
    defaults['UNITS'] = 'F'
    defaults['CITY'] = 'Cleveland'
    defaults['STATE'] = 'OH'
    defaults.save()

    gui = GUI()
    gui.run()
