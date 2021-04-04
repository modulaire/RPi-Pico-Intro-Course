import machine
import utime

myLed = machine.Pin(15, machine.Pin.OUT)

while True:
    myLed.toggle()
    utime.sleep(1)
