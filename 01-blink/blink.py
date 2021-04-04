#import the modules we will be using
import machine
import utime

#Create a variable for our led.
#Specify the pin number and designate it as an OUTPUT
myLed = machine.Pin(15, machine.Pin.OUT)

#Create a while loop
while True:
    myLed.toggle() #change Pin state
    utime.sleep(1) #wait one second
