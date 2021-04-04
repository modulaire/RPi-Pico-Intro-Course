import machine
from machine import PWM, Pin
import utime

servoPin = machine.Pin(13)
myServo = machine.PWM(servoPin)
myServo.freq(50);

button = machine.Pin(16, machine.Pin.IN)

while True:
    if button.value() == 1:
        for x in range(1000, 7000):
            myServo.duty_u16(x)
            utime.sleep(.001)
            
        for x in range(7000, 1000, -1):
            myServo.duty_u16(x)
            utime.sleep(.001)
