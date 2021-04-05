## pwm-fade example
**Using a single LED we will fade the luminosity on and off in a loop** <br />
We are here introducing a new function from the _machine_ module.<br />
<br />
PWM is short for __Pulse-Width Modulation__ <br />
PWM gives the impression of creating an analog signal since we work with output values ranging beyond 1 or 0. <br />
Where one may believe that we are changing the luminosity of an LED, the reality is that we are blinking it so fast that it deceives our eyes. <br />
<br />
The diagram below roughly illustrates this behavior. Where the red line is what we think we see, the blue line illustrates what is actually happening:

![pwm-diagram](pwm-diagram.png)

### Hookup guide:

![schematic](pwm-hookup.png)

