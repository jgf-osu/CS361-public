# gui/screens/home/encryptor.py

import PySimpleGUI as sg
import socket
import json
from weather.graphics import get_graphics_file
from gui import current

#################################################
# Here we communicate with Bill's microservice.
#################################################
# Works with this version:
#    https://tinyurl.com/demsar-encryptor

HOST = '127.0.0.1'
PORT = 12345 # hardcoded by Bill

def _encode(python_obj):
    json_str = json.dumps(python_obj)
    return json_str.encode()

def _decode(bytes_arr):
    str_ = bytes_arr.decode()
    return str_

def encrypt(msg):
    try:
        return _demsar(msg)
    except ConnectionRefusedError:
        txt = "Connection refused. Check if microservice is"\
            " running on port number %i." % PORT
        sg.Popup(txt)

def _demsar(msg):
    req = _encode(msg)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(req)
        response = _decode(s.recv(1024))
    return response

def encryptor_button():
    key = '-ENCRYPTOR-'
    tt = 'Encrypt the current conditions.'
    ico = get_graphics_file('spy')
    btn = sg.Button('Encrypt', key=key, tooltip=tt)
    return [btn, sg.Image(data=ico)]

def do_encryptor():
    plaintext = current.weather()
    cyphertext = encrypt(plaintext)
    if cyphertext:
        _report(plaintext, cyphertext)

def _report(plaintext, cyphertext):
    hr = '\n========================\n'
    text = '%sPLAINTEXT:\n%s%s%sCYPHERTEXT:\n%s%s' %\
        (hr, plaintext, hr, hr, cyphertext, hr)
    sg.popup_scrolled('Encrypted Weather Report', text, keep_on_top=True,
                      non_blocking=True)

