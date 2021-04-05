from machine import ADC
from utime import sleep

#create an object for our potentiometer on Pin(26)
pot = ADC(26)

while True:
    reading = pot.read_u16()
    print(reading)
    sleep(.01)