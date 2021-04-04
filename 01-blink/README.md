## Blink example
__First example using micropython on the Raspberry Pico__ <br/>
Modules used in _blink.py_ code:
- machine
- utime 

To change the on/off state of the led we are using the function _toggle()_ :

```python
myLed.toggle()
```

For more precise control we would use the following:

```python
myLed.on()
myLed.off()
```

or

```python
myLed.value(1)
myLed.value(0)
```

### Hookup guide:

__ALWAYS ADD A RESISTOR FOR THE LED!__ (220 or 330 ohm for example)

![schematic](RPico-blink.png)

