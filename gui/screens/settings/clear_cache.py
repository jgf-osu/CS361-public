# gui/screens/settings/clear_cache.py

import PySimpleGUI as sg
import weather.path
import weather.defaults
import os

def clear_cache_frame():
    btn0 = _clear_cache_button()
    btn1 = _show_cache_button()
    rows = list()
    rows.append([_clear_cache_text()])
    rows.append([sg.Push(), btn0, btn1, sg.Push()])
    return sg.Frame('Local Files', rows)

def _clear_cache_button():
    label = 'Clear Cache'
    tt = 'Delete all locally stored data.'
    key = '-Clear Cache-'
    return sg.Button(label, key=key, tooltip=tt)

def _show_cache_button():
    label = 'Show Cache'
    tt = 'Display a list of files in the cache.'
    key = '-Show Cache-'
    return sg.Button(label, key=key, tooltip=tt)

def _clear_cache_text():
    fpath = weather.path.file_in_this_dir(__file__, 'clear_cache.txt')
    with open(fpath, 'r') as f:
        txt = ' '.join(f.read().split('\n'))
        txt = txt % (weather.path.DATA_PATH,
                     weather.path.join('defaults.py'))
    return sg.Multiline(txt, size=(70,6), font=('sans', 10),
                        disabled=True)

def do_cache_action(event):
    if 'Show' in event:
        do_show_cache_action()
    elif 'Clear' in event:
        do_clear_cache_action()

def do_show_cache_action():
    text = '==================\n'
    text += '\n'.join(weather.path.list_data_filenames())
    sg.popup_scrolled('Local cache files:', text, keep_on_top=True,
                      non_blocking=True)


def do_clear_cache_action():
    if not _user_confirm(): return None
    errors = _delete_cache_files()
    if not errors:
        sg.popup("Cache successfully cleared.")
    else:
        _report_errors(errors)
    weather.defaults.save()
    
def _user_confirm():
    msg = "Really clear local cache?"
    r = sg.popup_yes_no(msg)
    return r == "Yes"

def _delete_cache_files():
    fails = list()
    for fpath in weather.path.list_data_files():
        try:
            os.unlink(fpath)
        except Exception as e:
            fails.append((fpath, str(e)))
    return fails

def _generate_error_report(errors):
    text = str()
    for fpath, exception in errors:
        text += "Could not delete file:\n\n%s\n\n" % fpath
        text += "Encountered the following exception:\n\n%s" % exception
        text += "\n\n" + '============='
    return text
    
def _report_errors(errors):
    text = _generate_error_report(errors)
    sg.popup_scrolled('Problems encountered', text, keep_on_top=True,
                      non_blocking=True)
    
