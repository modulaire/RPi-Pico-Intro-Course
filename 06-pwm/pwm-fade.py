# Example using PWM to fade an LED
from machine import Pin, PWM
from time import sleep

#Create PWM object, with LED on Pin(15)
pwm = PWM(Pin(15))

#Set the PWM frequency (pulse one thousand times per second)
pwm.freq(1000)

while True:
    #gradually turn on the LED
    for duty in range(65025):
        #PWM duty use 16-bit register from the Raspberry Pico
        pwm.duty_u16(duty)
        sleep(0.0001)
        
    #gradually turn off the LED
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)