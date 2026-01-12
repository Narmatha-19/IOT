from ctypes.wintypes import RGB
import time
import RPi.GPIO as GPIO
from colour import Color
from threading import Thread

GPIO.setmode(GPIO.BCM)

button = 27
#GPIO.setup(button,GPIO.IN)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
speed = 0.1
stop = False


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
        #print(r, g, b)

    # 0 - 225 for r, g, b
    def setRGBColor(self, r, g, b):
        r = (r  / 255) *100
        g = (g  / 255) *100
        b = (b  / 255) *100
        #print(r,g,b)

        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))

#led = RGBA(12, 13, 19)

def rgb_transition_thread():
    led = RGBA(12, 13, 19)

    while True:
        if stop:
            break

        for i in Color("violet").range_to(Color("indigo"), 1000):
            led.setRGB(i.rgb)
            time.sleep(speed / 100)
        for i in Color("indigo").range_to(Color("blue"), 1000):
            led.setRGB(i.rgb)
            time.sleep(speed / 100)
        for i in Color("blue").range_to(Color("green"), 1000):
            led.setRGB(i.rgb)
            time.sleep(speed / 100)
        for i in Color("green").range_to(Color("yellow"), 1000):
            led.setRGB(i.rgb)
            time.sleep(speed / 100)
        for i in Color("yellow").range_to(Color("orange"), 1000):
            led.setRGB(i.rgb)
            time.sleep(speed / 100)
        for i in Color("orange").range_to(Color("red"), 1000):
            led.setRGB(i.rgb)
            time.sleep(speed / 100)
        for i in Color("red").range_to(Color("white"), 1000):
            led.setRGB(i.rgb)
            time.sleep(speed / 100)
        for i in Color("white").range_to(Color("violet"), 1000):
            led.setRGB(i.rgb)
            time.sleep(speed / 100)


t = Thread(target = rgb_transition_thread)
t.start()
stime = time.time()

try:
    while True:
        if(GPIO.wait_for_edge(button, GPIO.RISING, timeout=5000)):
            print("Button key Down" + str(time.time()))
            stime = time.time()

        if(GPIO.wait_for_edge(button, GPIO.FALLING, timeout=5000)):
            print("Button key Up" + str(time.time()))
            ltime = time.time() - stime
            speed = ltime / 10
            print("Color change interval set to "+ str(speed))

except KeyboardInterrupt:
    stop = True
    t.join()
    GPIO.cleanup()
    print("Cleaned up...")
    