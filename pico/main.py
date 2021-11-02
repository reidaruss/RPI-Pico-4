from machine import Pin, I2C
from time import sleep
from dht import DHT11
from machine import UART

pin = Pin(15)
dht11 = DHT11(pin = Pin(15))

while True:
    dht11.measure()
    print((str(dht11.temperature)+","+str(dht11.humidity)).encode('utf-8'))
    sleep(2)