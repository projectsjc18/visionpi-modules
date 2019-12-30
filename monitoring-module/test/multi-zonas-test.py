# importa la funcion de lectura para GPIO
import RPi.GPIO as GPIO
import time
import datetime
import socket
# obtiene el valor de la Mac en decimal y hexagecimal
from uuid import getnode as get_mac
mac = get_mac()
# print (hex(mac))

nombrehost = socket.gethostname()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
estado_zn1 = 3
estado_zn2 = 3
estado_zn3 = 3
while True:
    # Evalua el estado de la zona por medio del GPIO 18
    inputValue = GPIO.input(18)
    if (inputValue is True and estado_zn1 != 1):
        fecha_actual = datetime.datetime.now()
        # mensaje = "Alarma activa en " + nombrehost + "a las" + fecha_actual
        print("Alarma activa Zona 1 ", nombrehost, " a las ", fecha_actual)
        estado_zn1 = 1
        time.sleep(0.5)
    time.sleep(1)

    if (inputValue is False and estado_zn1 != 2):
        fecha_actual = datetime.datetime.now()
        print("Zona 1 restaurada a las", fecha_actual)
        estado_zn1 = 2
        time.sleep(0.5)

    time.sleep(1)

    # Evalua el estado de la zona por medio del GPIO 23
    inputValue = GPIO.input(23)
    if (inputValue is True and estado_zn2 != 1):
        fecha_actual = datetime.datetime.now()
        # mensaje = "Alarma activa en " + nombrehost + "a las" + fecha_actual
        print("Alarma activa Zona 2 ", nombrehost, " a las ", fecha_actual)
        estado_zn2 = 1
        time.sleep(0.5)
    time.sleep(1)

    if (inputValue is False and estado_zn2 != 2):
        fecha_actual = datetime.datetime.now()
        print("Zona 2 restaurada a las ", fecha_actual)
        estado_zn2 = 2
        time.sleep(0.5)

    time.sleep(1)

    inputValue = GPIO.input(24)
    if (inputValue is True and estado_zn3 != 1):
        fecha_actual = datetime.datetime.now()
        # mensaje = "Alarma activa en " + nombrehost + "a las" + fecha_actual
        print("Alarma activa Zona 3 ", nombrehost, " a las ", fecha_actual)
        estado_zn3 = 1
        time.sleep(0.5)
    time.sleep(1)

    if (inputValue is False and estado_zn3 != 2):
        fecha_actual = datetime.datetime.now()
        print("Zona 3 restaurada a las ", fecha_actual)
        estado_zn3 = 2
        time.sleep(0.5)

    time.sleep(1)
