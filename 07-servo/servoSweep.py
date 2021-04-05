from machine import PWM, Pin
from utime import sleep

# Create our servo object
myServo = PWM(Pin(16))

# set frequency to 50, required for servo motors
myServo.freq(50);

# define minimum and maximum duty variables, compatible with our servo motor
minDuty = 1900
maxDuty = 7200

while True:

    print("move left")
    for duty in range(minDuty, maxDuty):
        myServo.duty_u16(duty)
        sleep(.001)

    print("move right")
    for duty in range(maxDuty, minDuty, -1):
        myServo.duty_u16(duty)
        sleep(.001)
