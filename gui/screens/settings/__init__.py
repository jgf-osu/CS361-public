# gui/screens/settings/__init__.py

import PySimpleGUI as sg
from gui.screens import home
from .interface import SettingsInterface

def show():
    ui = SettingsInterface()
    user_exit = False
    while not user_exit:
        event = ui.read()
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            user_exit = ui.exit()
        if event == '-[BTN] SAVE-':
            ui.save()
        if event == '-[BTN] HOME-':
            user_exit = ui.exit()
        if event == '-[BTN] SAVE&HOME-':
            ui.save()
            user_exit = ui.exit()
    ui.close()
    home.show()
