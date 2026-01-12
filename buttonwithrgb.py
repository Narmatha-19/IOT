from ctypes.wintypes import RGB
import time
import RPi.GPIO as GPIO
from colour import Color
from threading import Thread

GPIO.setmode(GPIO.BCM)

button = 27
#GPIO.setup(button,GPIO.IN)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
speed = 0.1


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
        for i in Color("red").range_to(Color("blue"), 10):
            led.setRGB(i.rgb)
            time.sleep(speed)

        for i in Color("blue").range_to(Color("red"), 10):
            led.setRGB(i.rgb)
            time.sleep(speed)

t = Thread(target = rgb_transition_thread)
t.start()
stime = None

try:
    while True:
        if(GPIO.input(button) == GPIO.HIGH):
            print("Button pressed..."+str(time.time()))
            if stime is None:
                stime = time.time()
            else:
                speed = time.time() - stime
                print("Current speed is "+ str(speed))
                stime = None
            time.sleep(0.01)

except KeyboardInterrupt:
    t.stop()
    GPIO.cleanup()
    print("Cleaned up...")
    
    
        



