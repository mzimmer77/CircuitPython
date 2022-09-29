# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
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

https://iad.cdn.nv.instructuremedia.com/originals/o-5rHQz7CxZNjN6wtBEeMQcXxsQk5kA9r6/transcodings/t-5rQwrZyxD5Dfk3fN3EBfTk3tWPozGAF2.mp4?&Expires=1664374995&Signature=DOKfQ60o9le-rT9BksZlDIKUNYTd6KXlkw~mapKYPEP1KZro9unWSBlwYqCU2Jae0Y-GCpSjKmSCh-wMWXFrGdAYVhQ4u~915OajmZROQrZ9Wm8Qss6QEnIDwXKgVlOVFv4nx2ctZujzRkirjMwt1LE2P3ekONw2Lzc3Ui2ik5X2FkdvA0EEj19A6tUUcufW8idjbRbp3a~yb7qBghNcusRCW9HbyckOIpaf3xikH1mDz-zw493DIM~1tLIOtwdHtBdA-H1QwWoliXICc-K5YbCd7~PFB0up0EZVxqBcXX4w1-keelSSav6AAL2JokwRZiwRNx6BCEV9A4Jxts1SSQ__&Key-Pair-Id=APKAJLP4NHW7VFATZNDQ



And here is how you should give image credit to someone, if you use their work:

Image credit goes to matthias



### Wiring
https://www.tinkercad.com/things/l74pWa2Bojx-brave-turing/editel?tenant=circuits

### Reflection
I got some help from Mr H in order to learn python and vscode.




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

https://iad.cdn.nv.instructuremedia.com/originals/o-5YnGRJjECHz2rELYMEnSKeKAbSwqC8Wk/transcodings/t-5YwxWG74a9m7XzPXDerVhP38Fr7X8omx.mp4?&Expires=1664375418&Signature=sp-fOIDnlGlWK8Vd5s0BrBiREQz4I2LMfssDhpHeYqYUGVtCklYarHgy3lptLBlGQB764uKpawIZHFoxuyAqSVZRyCtvKndF2J4I32IzrEgJqd9qEl-DF~b51ltiiF6VvrPZyeKy1iIO8bsUjWjbpfxQlsQs5K5vnY2bgUeZH8OTG-rFNM4opWdh8TkchHwOntpUTB3S-wFBYnNkZ8zedF9rJFMYLEFD0ZdLGmheeRw7X4gBvgdRW7CPAN3hK6t3hDm2vbK1G9GUn0iWOnnzEYXLOWzDLMvbSSdUI0XXbgXsZgJx95Q4XfNk0OiLfUWPkyhbBQccGY6oZ6-oTrdetA__&Key-Pair-Id=APKAJLP4NHW7VFATZNDQ

### Wiring
![image](https://user-images.githubusercontent.com/112961434/192555694-4ad0eed2-1c11-4fa1-b789-35e882e869b6.png)
Kattni Rembor, Jeff Epler, Carter Nelson, lady ada
### Reflection
it was a lot more challenging to use a servo because I had to rememeber how to wire and use a servo but google was my friend.


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

https://user-images.githubusercontent.com/112961434/193045428-e40a7dd3-4e1c-4088-9459-a113abd227fd.mp4


~~~






And here is how you should give image credit to someone, if you use their work:

Image credit goes to matthias



### Wiring
https://www.tinkercad.com/things/l74pWa2Bojx-brave-turing/editel?tenant=circuits

### Reflection
I got some help from Mr H in order to learn python and vscode.



## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence
https://mail.google.com/mail/u/0?ui=2&ik=6c4263679f&attid=0.1&permmsgid=msg-f:1745134024592886924&th=1837f626354e8c8c&view=att&disp=safe

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
