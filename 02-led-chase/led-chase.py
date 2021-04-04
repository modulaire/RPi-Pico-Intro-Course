from machine import Pin
from utime import sleep

#create a variable for each LED
#assign each LED a different Pin number and designate it as output
ledA = Pin(15, Pin.OUT)
ledB = Pin(14, Pin.OUT)
ledC = Pin(13, Pin.OUT)

myDelay = 0.5 # myDelay is half of a second

while True:
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
    #turn off ledC and return to the beginning of the loop
