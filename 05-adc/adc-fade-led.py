# Analog input controls intensity of LED output 
from machine import Pin, PWM, ADC
from utime import sleep

#Create Analog and PWM objects, designate their Pin numbers
adc = ADC(Pin(26))
pwm = PWM(Pin(15))

pwm.freq(1000)

while True:
	duty = adc.read_u16()
	print(duty)
	sleep(.01) # delay buffer necessary when printing to serial port
	pwm.duty_u16(duty)