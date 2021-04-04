from machine import Pin
from utime import sleep

ledA = Pin(15, Pin.OUT)
ledB = Pin(14, Pin.OUT)
ledC = Pin(13, Pin.OUT)

myDelay = 0.2 # myDelay is half of a second
button = Pin(11, Pin.IN)

while True:
    if button.value() == 1:
        for x in range(10):
            #turn on ledA and wait half a second
            ledA.value(1)
            sleep(myDelay)
            ledA.value(0)
            #turn off ledA then turn on ledB and wait half a second
            ledB.value(1)
            sleep(myDelay)
            ledB.value(0)
            #turn off ledB then turn on ledC for wait a second
            ledC.value(1)
            sleep(myDelay)
            ledC.value(0)
