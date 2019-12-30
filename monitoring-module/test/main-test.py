# importa la funcion de lectura para GPIO
# import RPi.GPIO as GPIO
import time
import datetime
import socket
import json
import requests
from commons import Database as db
# obtiene el valor de la Mac en decimal y hexagecimal
from uuid import getnode as get_mac
mac = get_mac()
# print (hex(mac))


def formatDate(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def get_access_token():
    token = 'am9obmRvZTpBM2RkajN3'
    api_url_base = 'https://127.0.0.1:8080/auth/access_token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               'Authorization': 'Basic {0}'.format(token)}
    payload = {'grant_type': 'password',
               'username': 'johndoe',
               'password': 'A3ddj3w'}
    response = requests.post(api_url_base, verify=False, headers=headers, data=payload)
    print(response)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def send_event(message):
    api_token = get_access_token()
    api_url_base = 'https://127.0.0.1:8080/v1/monitoring/events'
    # api_url_base = 'http://127.0.0.1:3000/monitoring/events'
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token['token']['accessToken'])}
    api_url = '{0}'.format(api_url_base)
    response = requests.post(api_url, verify=False, headers=headers, json=message)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


nombrehost = socket.gethostname()
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(24, GPIO.IN)
estado = 3
while True:
    inputValue = True  # GPIO.input(24)
    if (inputValue is True and estado != 1):
        fecha_actual = datetime.datetime.now()
        # message = "Alarma activa en " + nombrehost + "a las" + fecha_actual
        message = {
                      'account': 'VP99999',
                      'device': 'GPIO',
                      'events': [{'type': 'Alarm',
                                  'event': 'Alarma activa en ' + nombrehost,
                                  'registerdate': 'generateDate()'}],
                      'status': 'Active',
                      'eventdate': formatDate(fecha_actual)
                  }
        response = send_event(message)
        print(response)
        estado = 1
        time.sleep(0.5)
        time.sleep(1)

    if (inputValue is False and estado != 2):
        fecha_actual = datetime.datetime.now()
        message = {
                      'account': 'VP99999',
                      'device': 'GPIO',
                      'events': [{'type': 'Alarm',
                                  'event': 'Alarma restaurada en ' + nombrehost
                                  , 'registerdate': 'generateDate()'}],
                      'status': 'Restored',
                      'eventdate': formatDate(fecha_actual)
                  }
        response = send_event(message)
        print(response)
        # print("Estado en alarma restaurada a las", fecha_actual)
        estado = 2
        time.sleep(0.5)
        time.sleep(1)
