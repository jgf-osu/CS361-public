import gui
from weather.configurator import DefaultSetter

if __name__ == '__main__':
    # Create some default values. These values will be used if and
    # only if no others have been provided previously.
    defaults = DefaultSetter()
    defaults['UNITS'] = 'F'
    defaults['CITY'] = 'Cleveland'
    defaults['STATE'] = 'OH'    
    defaults.save()

    # Run the GUI client.
    gui.run()
