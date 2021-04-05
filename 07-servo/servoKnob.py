from machine import Pin, ADC, PWM
from utime import sleep

# create objects for our servo and potentiometer
myServo = PWM(Pin(16))
pot = ADC(26)

# set frequency to 50, required for servo motors
myServo.freq(50)

# define minimum and maximum values received from potentiometer
minPotVal = 176
maxPotVal = 65535

# define minimum and maximum duty values for the servo
minDuty = 1900
maxDuty = 7200

'''
create constrain() and map() functions for managing and applying
range values differing between INPUT and OUTPUT values
'''
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# while loop
while True:
    reading = pot.read_u16()
    print(reading)
    servoPulse = _map(reading, minPotVal, maxPotVal, minDuty, maxDuty)
    duty = constrain(servoPulse, minDuty, maxDuty)
    myServo.duty_u16(duty)

    sleep(.01) # sleep added for print buffer
