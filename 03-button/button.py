'''
Basic Button example
--------------------
10K pull-down resistor is required on breadboard.
Internal pull-down resistor can likewise be activated.
'''

from machine import Pin
from utime import sleep

#create variable for our input button
button = Pin(11, Pin.IN)

#include Pin.PULL_DOWN to activate internal pull-down resistor, as follows:
#button = Pin(11, Pin.IN, Pin.PULL_DOWN)

while True:
    #if button is pushed, then print message
    if button.value() == 1:
        print("Button pressed!")
        sleep(.5) #short delay avoids printing message thousands of times per second
