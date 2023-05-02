# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Tempature Sensor](#TempSensor)
* [RotaryEncoder](#RotaryEncoder)
* [Photointerrupter](#Photointerrupter)
---

## Hello_CircuitPython

### Description & Code
For this assignment we had to learn vscode and we made a button blink red

Here's how you make code look like code:

```python
Code goes here
import board
import neopixel
import time
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((255, 0, 0))
    print("Red")
    time.sleep(0.5)

    dot.fill((255, 0, 255))
    print("Purple")
    time.sleep(0.5)
```


### Evidence



https://user-images.githubusercontent.com/112961434/193046589-a9bb4d3b-664a-4453-8a38-d1be18a54cc4.mp4




And here is how you should give image credit to someone, if you use their work:

Image credit goes to matthias



### Wiring
https://www.tinkercad.com/things/l74pWa2Bojx-brave-turing/editel?tenant=circuits

### Reflection
I got some help from Mr H in order to learn python and vscode. I also forgot to have the library and you should remember to insert the library for neopixel.




## CircuitPython_Servo

### Description & Code
this assignment we were asked to move a servo 180 degrees
```python
Code goes here
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence


https://user-images.githubusercontent.com/112961434/193046467-25b1430d-01c0-4595-9e3e-dfa70ef56894.mp4



### Wiring
![image](https://user-images.githubusercontent.com/112961434/192555694-4ad0eed2-1c11-4fa1-b789-35e882e869b6.png)
Kattni Rembor, Jeff Epler, Carter Nelson, lady ada
### Reflection
it was a lot more challenging to use a servo because I had to rememeber how to wire and use a servo but google was my friend. Again, make sure you have the correct libraries for servos in there. Additionally, having it go 5 degrees at a time is crucial.


## UltraSonic Senor

### Description & Code
we had to make an ultrasonic sensor that faded the color of the board LED
```
#thanks graham, grant, and mason for the code
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
matthias = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
matthias.brightness = .3  #setting the brightness of the light, from 0-1 brightness

while True:
    try:
        cm = sonar.distance
        simpleio.map_range(cm, 0, 20, 3, 20)
        print((sonar.distance))
        if cm < 7.5:
            red = simpleio.map_range(cm, 0, 6.5, 255, 0)# mapping the colors to the length
            green = simpleio.map_range(cm, 5, 7.5, 0, 230)
            matthias.fill((red, green, 0))
        if cm > 7.5 and cm < 12.5:
            green = simpleio.map_range(cm, 7.5, 10, 255, 0)
            blue = simpleio.map_range(cm, 9, 12.5, 0, 230)
            matthias.fill((0, green, blue))
        if cm > 12.5 and cm < 17.5:
            blue = simpleio.map_range(cm, 12.5, 15, 255, 0)
            red = simpleio.map_range(cm, 14, 17.5, 0, 240)
            matthias.fill((red, 0, blue))
        time.sleep(0.01)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

### Evidence
```



https://user-images.githubusercontent.com/112961434/193046166-11c7c9fa-54c6-4ee5-ade7-2176b5cff94f.mp4






And here is how you should give image credit to someone, if you use their work:

Image credit goes to matthias



### Wiring
![193045742-26a5ac02-6881-416c-9d54-af293deceae0](https://user-images.githubusercontent.com/112961434/193048819-4750fa1a-3b1d-4859-a733-ea9df81ee28b.png)
elias https://github.com/egarcia28/CircuitPython
### Reflection
this assignment was difficult because of the fading of the light and finding the right fade. the colors also have to be right if you want to make a rainbow. Using maap functions may be difficult but it makes everything a lot smoother.


## CircuitPython_LCD

### Description & Code

```python
Code goes here
Grant Gastinger https://github.com/ggastin30/CPython
Import necessary libraries
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
from digitalio import DigitalInOut, Direction, Pull

Initialize input/output pins and variables
i2c = board.I2C() # Create an I2C object
btn = DigitalInOut(board.D2) # Initialize the button
btn.direction = Direction.INPUT
btn.pull = Pull.UP
clickCount = 0 # Initialize the click count to 0

switch = DigitalInOut(board.D7) # Initialize the switch
switch.direction = Direction.INPUT
switch.pull = Pull.UP

Initialize LCD object and display name
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
lcd.print("Matthias")

Main loop
while True:
if not switch.value: # Check if the switch is flipped
if not btn.value: # Check if the button is pressed
lcd.clear() # Clear the screen
lcd.set_cursor_pos(0, 0) # Set the cursor to the top left corner
lcd.print("Click Count:") # Print the title
lcd.set_cursor_pos(0,13) # Set the cursor to the 14th position on the first row
clickCount = clickCount + 1 # Increment click count
lcd.print(str(clickCount)) # Print the updated click count
else:
pass
else:
if not btn.value: # Check if the button is pressed
lcd.clear() # Clear the screen
lcd.set_cursor_pos(0, 0) # Set the cursor to the top left corner
lcd.print("Click Count:") # Print the title
lcd.set_cursor_pos(0,13) # Set the cursor to the 14th position on the first row
clickCount = clickCount - 1 # Decrement click count
lcd.print(str(clickCount)) # Print the updated click count
else:
pass
time.sleep(0.1) # Sleep for debounce. This is to make sure we don't register multiple clicks.
```

### Evidence


https://user-images.githubusercontent.com/112961434/193046801-679b4d02-3eee-4f74-8c34-5ac0fc597b24.mp4


### Wiring
![193033429-e5198fd6-79fd-4952-a702-64e0c3bba90c](https://user-images.githubusercontent.com/112961434/193047265-43d4e611-0c68-453c-8ac3-ebb8ee76e326.png)
###thanks elias https://github.com/egarcia28/CircuitPython
### Reflection
this was by far the hardest assignment but I had done something like this last year and my prior knowledge along with the help of classmates gave me what I needed to understand and complete the assignment. Make sure you have LCD library. Having the position of where it started was just as important.




## Motor Control

### Description & Code
we had to make a potentiometer control a DC motor while using a battery pack.
```python
Code goes here
#thanks https://github.com/willhunt914
#thanks https://github.com/nbednar2929
import board #import files
import time
from analogio import AnalogOut, AnalogIn
import simpleio

motor = AnalogOut(board.A1) #motor ouput 
ptmr = AnalogIn(board.A0) #potentiometer input

while True:
    print(simpleio.map_range(ptmr.value, 96, 65520, 0, 65535)) #print my potentiometer value
    motor.value = int(simpleio.map_range(ptmr.value, 96, 65520, 0, 65535)) #push potentiometer value to motor
    time.sleep(.1) #print delay 
```

### Evidence


https://user-images.githubusercontent.com/112961434/200870809-63e3a476-a707-4634-a149-70ff03f4fc09.mp4


### Wiring
![image](https://user-images.githubusercontent.com/112961434/200871929-46aee14c-0fb9-48fa-a15a-a6ea1738df8c.png)
https://github.com/willhunt914/CirclePython#Moter_Control
### Reflection
make sure you] double checking your wiring before you plug in the bateries so you dont fry anything or have magic smoke. For the diodes the power flows in the direction of the silver cap. For the transistor, facing the flat side the power flows from left to right. remember to connect the gnd with a wire


## TempSensor

### Description & Code
we had to use a tempature sensor and an LCD to display it.
```python
Code goes here
#code from wmorela54
import board
import analogio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


TMP36_PIN = board.A0  # Analog input connected to TMP36 output.

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16) #0x27 or 0x3f

# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10

# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN)
desired_temp_min = 70
desired_temp_max = 78

while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a  few seconds before looping again.
    print("Temperature: {}C {}F".format(temp_C, temp_F))
    time.sleep(3.0)
    if temp_F >= desired_temp_min and temp_F <= desired_temp_max:
        lcd.clear()
        lcd.print("It feels great  in here")
    if temp_F < desired_temp_min:
        lcd.clear()
        lcd.print("brrr too cold")
    if temp_F > desired_temp_max:
        lcd.clear()
        lcd.print("To hot")
    time.sleep(2.0)
```

### Evidence


https://user-images.githubusercontent.com/112961434/225632084-8f5b42dc-fb0c-4641-89a0-a7961f27e5d4.mov


### Wiring
![image](https://user-images.githubusercontent.com/112961434/225632332-c6d4f69d-ae26-435a-8255-7c3c73feb427.png)
(credit cooper)
### Reflection
this was difficult until my bestfriend cooper let me borrow his code and wiring and video and that made it a whole lot easier. Having different points makes it easier to find a error or to see tempature. The delay is just as important and helps you get good readings.

## RotaryEncoder

### Description & Code
For this assignment we were told to use a rotary encoder which when integrated with an LCD screen and LED's act as a traffic light.


```python
Code goes here
##thanks river!
import rotaryio
import board
import digitalio
import neopixel
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

led: neopixel.Neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1) # initialization of hardware
print("neopixel")

led.brightness = 0.1

button = digitalio.DigitalInOut(board.D12)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

colors = [("stop", (255, 0, 0)), ("caution", (128, 128, 0)), ("go", (0, 255, 0))]

encoder = rotaryio.IncrementalEncoder(board.D10, board.D9, 2)
last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        lcd.clear()
        lcd.print(colors[position % len(colors)][0])
    if(not button.value):
        led[0] = colors[position % len(colors)][1]
    last_position = position

```

### Evidence
https://rivques.github.io/docs/trafficlight.gif
link to a working video (mine wouldn't fit)
### Wiring
![image](https://user-images.githubusercontent.com/112961434/227950893-17176ca7-6371-4b56-a795-afd7f4071b63.png)

### Reflection
I’m really proud of how I did the menu logic for this project. The encoder library gives a position in “clicks from startup position.” I have a list of menu strings and colors, like this:

colors = [("stop", (255, 0, 0)), ("caution", (128, 128, 0)), ("go", (0, 255, 0))]
Then, to get the color I should be using, I can simply take the element of the list at encoder.position % len(colors). This will smoothly loop around the list. Also, once again, our hardware is not quite the default configuration. This means in the initialization of the encoder library I have to set the divisor argument of the rotaryio.IncrementalEncoder to 2 instead of 4.

## Photointerrupter

### Description & Code
Use a photinerrupter and track the amount of interrupts on an LCD screen.


```python
Code goes here
import time #imports
import rotaryio
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16) #identify LCD screen

photoint = DigitalInOut(board.D7) #identify photointerrupter
photoint.pull =Pull.UP #pull up photointerrupter
counter = 0 #create counter set to zero

while True:
    if photoint.value == True: #if photointerrupter 
        counter = counter + 1 #add to counter
        lcd.clear()
        lcd.color = [0, 100, 0]
        lcd.set_cursor_pos(0, 0) #set lcd cursor position
        lcd.print("Interrupts:" + str(counter)) #print interrupts and counter on lcd
        time.sleep(.5) #0.5sec delay
```

### Evidence
https://user-images.githubusercontent.com/91289646/227621696-b567911c-63c2-4ace-9a62-63967fb9f7ea.PNG
### Wiring
![image](https://user-images.githubusercontent.com/112961434/227956549-a2832999-d79f-4291-b89f-b64997d88a37.png)

### Reflection
Thanks nick bendar for help with the wiring and starting the code
All it requred was creating a counter and initalizing my photointerrupter as well as pulling it up. When the photointerrupter is interrupted the counter goes up by one. it was kinda like an assignment we did earlier.
## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
