import utime

With utime you can get the local time as below.

#Get the current time
current_time = utime.localtime()
#Format the current time as "dd/mm/yyyy HH:MM"
formatted_time = "{:02d}/{:02d}/{} {:02d}:{:02d}".format(current_time[2], current_time[1], current_time[0], current_time[3], current_time[4])

import network
import socket
from time import sleep
from picozero import pico_temp_sensor
import machine


ssid = 'ADDIDHERE'
password = 'ADDPASSWORDHERE'


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def webpage(temperature):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
	    <body style="background-color:#000000">
            <p> </p>
	    <p style="color:#00ff41">Temperature is {temperature}</p>
            <p> </p>
            <p style="color:#00ff41"><a href="https://plwt.github.io/tfpico.html">But what are you really?</a></p> 
            </body>
            </html>
            """
    return str(html)


def serve(connection):
    #Start a webserver
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        temperature = pico_temp_sensor.temp
        html = webpage(temperature)
        client.send(html)
        client.close()


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
