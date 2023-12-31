# client-demo.py

import socket
import weather.service as ws

# Launch this script after you've launched listen.py

if __name__ == '__main__':
    server = ws.WeatherService()      
    
    # request NOAA NWS report for a US city/town/etc.
    request = {
        'request-type':'current-conditions',
        'city': input("Enter a US city/town/etc: "),
        'state': input("Enter a US state: ")
    }

    print("CLIENT: Sending request to port %i." % server.port)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        payload = ws.encode(request)
        s.connect((server.host, server.port))
        s.sendall(payload)
        response = ws.decode(s.recv(1024))

        location = '%s, %s' % (request['city'], request['state'])
        report = "Weather conditions requested for %s." % location
        print(report)
        print(response)
        
