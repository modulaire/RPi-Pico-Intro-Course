import machine
import utime

#create an object for our potentiometer on Pin(26)
pot = machine.ADC(26)

while True:
    reading = pot.read_u16()
    
    print(reading)
    utime.sleep(.01)