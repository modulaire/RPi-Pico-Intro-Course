'''
Button-Led-Chase example
------------------------
Internal pull-down resistor is activated instead of adding one to the breadboard.
'''

from machine import Pin
from utime import sleep

button = Pin(11, Pin.IN, Pin.PULL_DOWN)

ledA = Pin(15, Pin.OUT)
ledB = Pin(14, Pin.OUT)
ledC = Pin(13, Pin.OUT)

myDelay = 0.25 # myDelay is quarter of a second

while True:
    if button.value() == 1:
        print("Button pressed!")
        #for loop condition. Repeats 5 times
        for x in range(5):
            ledA.on()
            sleep(myDelay)
            ledA.off()
            ledB.on()
            sleep(myDelay)
            ledB.off()
            ledC.on()
            sleep(myDelay)
            ledC.off()

