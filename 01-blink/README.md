## Blink example
**First example using micropython on the Raspberry Pico** <br />
Python Modules used:
- machine
- utime
<br />
To change the on/off state of the led we are using the function toggle()<br />
For more precise control we would use the folowing:
```
myLed.on()
myLed.off()

-- or --

myLed.value(1)
myLed.value(0)
```

**ALWAYS ADD A RESISTOR FOR THE LED!** (220 or 330 ohm for example)
### Hookup guide:
![schematic](RPico-blink.png)

