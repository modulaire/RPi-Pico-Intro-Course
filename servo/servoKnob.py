import machine
import utime

servoPin = machine.Pin(13)
myServo = machine.PWM(servoPin)
myServo.freq(50)
pot = machine.ADC(26)

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    reading = pot.read_u16()
    
    print(reading)
    servoPulse = _map(reading,176,65535,1000,7000)
    servoPulse = constrain(servoPulse, 1000,7000)
    myServo.duty_u16(servoPulse)
    utime.sleep(.01)
    