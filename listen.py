import sys
import random
from weather.configurator import Configurator
from weather.service import WeatherService

def cli_parse():
    argv, argc = sys.argv, len(sys.argv)
    port = random.randint(49152, 65535)
    if argc > 1:
        if argv[1] == '-h' or argv[1] == '--help':
            with open('help/listen.txt', 'r') as f:
                sys.stderr.write(f.read())
            return
        else:
            try:
                port = int(argv[1])
            except ValueError:
                sys.stderr.write("Invalid port number: %s.\n" % argv[1])
                sys.stderr.write("Choosing an arbitrary port instead.\n")

    ws = WeatherService('127.0.0.1', port)
    while True:
        ws.listen()

if __name__ == '__main__':
    cli_parse()
