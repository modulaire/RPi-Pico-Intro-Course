## led-chase example
**Building upon the Blink example, 3 LEDs are animated in sequence** <br />
We move on to import only the functions we need from modules instead of calling the entire module.<br />
This reduces the amount of typing required in the code.<br />
<br />

Example when importing only the _Pin_ function from module _machine_ :

```python
myLed = Pin(15, Pin.OUT)
```

will act the same as

```python
myLed = machine.Pin(15, machine.Pin.OUT)
```

**Functions imported from modules:**
- Pin from machine
- sleep from utime

### Hookup guide:

**ALWAYS ADD A RESISTOR FOR THE LEDS!** (220 or 330 ohm for example)

![schematic](RPi-led-chase.png)

