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