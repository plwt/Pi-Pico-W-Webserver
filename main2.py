import network
import socket
from time import sleep
from picozero import pico_temp_sensor
from machine import ADC

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
    # Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <body style="background-color:#000000">
            <p> </p>
            <p style="color:#00ff41; font-size:50px">Temperature is {temperature} *C</p>
            <p> </p>
            </body>
            </html>
            """
    return str(html)


# Temperature Sensor
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
 
def temperature():
    temperature_value = sensor_temp.read_u16() * conversion_factor 
    temperature_Celcius = (27 - (temperature_value - 0.706)/0.00172169) - 4 
    utime.sleep(2)
    return temperature_Celcius


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
        temperature = temperature_Celcius
	      html = webpage(temperature)
        client.send(html)
        client.close()


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
