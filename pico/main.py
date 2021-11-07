from machine import Pin, I2C
from time import sleep
from dht import DHT11
from machine import UART

import _thread

pin = Pin(15)
dht11 = DHT11(pin = Pin(15))

def pollAndTransmit():
    while True:
        dht11.measure()
        print((str(dht11.temperature)+","+str(dht11.humidity)).encode('utf-8'))
        sleep(10*60)

def listen():
    while True:
        print("Listening")


_thread.start_new_thread(pollAndTransmit, ())
_thread.start_new_thread(listen())
