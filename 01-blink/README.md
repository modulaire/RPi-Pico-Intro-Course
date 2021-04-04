## Blink example
__First example using micropython on the Raspberry Pico__ <br/>
Python Modules used:
- machine
- utime 
<br/>
To change the on/off state of the led we are using the function toggle()<br/>
For more precise control we would use the folowing:<br/>
```python
myLed.on()
myLed.off()
```<br/>
__or__<br/>
```python
myLed.value(1)
myLed.value(0)
```<br/>

__ALWAYS ADD A RESISTOR FOR THE LED!__ (220 or 330 ohm for example)
### Hookup guide:
![schematic](RPico-blink.png)

