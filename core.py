from ctypes.wintypes import RGB
import time
import RPi.GPIO as GPIO
import math
from colour import Color

class RGBA():
    def __init__(self, r, g, b):
        GPIO.setmode(GPIO.BCM)
        channel = [r, g, b]
        for c in channel:
            GPIO.setup(c, GPIO.OUT)
        self.r = GPIO.PWM(r, 120) # channel = 12 frequency = 60Hz
        self.g = GPIO.PWM(g, 120)
        self.b = GPIO.PWM(b, 120)
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)

    #0 - 100 (For colours module)
    def setRGB(self, rgb):
        r = rgb[0] * 100 #default value in Color module is 1 - so we multiplied with 100
        g = rgb[1] * 100
        b = rgb[2] * 100
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))
        print(r, g, b)

    # 0 - 225 for r, g, b
    def setColor(self, r, g, b):
        r = (r  / 255) *100
        g = (g  / 255) *100
        b = (b  / 255) *100
        print(r,g,b)

        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))

led = RGBA(12, 13, 19)
#led.setColor(255, 0, 0)
#led.setRGB((100, 0 ,0))
#time.sleep(10)

#rtb = Color("red").range_to(Color("blue"), 15) red to blue
#btr = Color("blue").range_to(Color("red"), 15) blue to red

while True:
    
    for i in Color("red").range_to(Color("blue"), 15):
        led.setRGB(i.rgb)
        time.sleep(0.5)

    for i in Color("blue").range_to(Color("red"), 15):
        led.setRGB(i.rgb)
        time.sleep(0.5)
        
GPIO.cleanup()       

#another type displaying different colors by manually entering..
for i in range(10):
    led.setRGB(Color(input("Enter the Color_Name:  ")).rgb)
    time.sleep(0.5)
GPIO.cleanup()


