# imports
import time
import datetime
import socket
# importa la funcion de lectura para GPIO
# import RPi.GPIO as GPIO
# Commons
from commons import Database, Dates
# obtiene el valor de la Mac en decimal y hexagecimal
from uuid import getnode as get_mac
mac = get_mac()
# print (hex(mac))


class Monitoring():

    def __init__(self):
        self.name_host = socket.gethostname()
        self.dates = Dates()
        self.db = Database()

    def monitoring_events(self):
        self.db.loadDatabase()
        nombrehost = socket.gethostname()
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(24, GPIO.IN)
        estado = 3
        while True:
            inputValue = True  # GPIO.input(24)
            if (inputValue is True and estado != 1):
                current_date = str(datetime.datetime.now())
                print('current_date', current_date)
                account = 'VP99999'
                device = 'GPIO'
                type = 'Alarm'
                even = 'Alarma activa en ' + nombrehost
                status = 'Active'
                eventdate = current_date
                event = {
                              'account': account,
                              'device': device,
                              'events': [{'type': type,
                                          'event': even,
                                          'registerdate': eventdate}],
                              'status': status,
                              'eventdate': eventdate
                          }
                # response = send_event(event)
                # print(response)
                self.db.save_event(account, device, even, type, status,
                                   eventdate)
                estado = 1
                time.sleep(0.5)
                time.sleep(1)

            if (inputValue is False and estado != 2):
                current_date = str(datetime.datetime.now())
                print('current_date', current_date)
                account = 'VP99999'
                device = 'GPIO'
                type = 'Alarm'
                even = 'Alarma activa en ' + nombrehost
                status = 'Active'
                eventdate = current_date
                event = {
                              'account': account,
                              'device': device,
                              'events': [{'type': type,
                                          'event': even,
                                          'registerdate': eventdate}],
                              'status': status,
                              'eventdate': eventdate
                          }
                # response = send_event(event)
                # print(response)
                self.db.save_event(account, device, even, type, status,
                                   eventdate)
                print("Estado en alarma restaurada a las", current_date)
                estado = 2
                time.sleep(0.5)
                time.sleep(1)
