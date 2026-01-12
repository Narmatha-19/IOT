"""import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
channel = [12, 13, 19]

for c in channel:
    GPIO.setup(c, GPIO.OUT)

red_pwm = GPIO.PWM(12, 1)  # 100Hz frequency
green_pwm = GPIO.PWM(13, 1)
blue_pwm = GPIO.PWM(19, 1)

for i in red_pwm , green_pwm, blue_pwm:
    i.start(10)

while True:
    
    for r in range(75):
        red_pwm.ChangeDutyCycle(r)

        for g in range(50,75,5):
            green_pwm.ChangeDutyCycle(g)

            for b in range(70, 100, 10):
                blue_pwm.ChangeDutyCycle(b)

red_pwm.stop()
green_pwm.stop()
blue_pwm.stop()
GPIO.cleanup()"""

import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
channel = [12, 13, 19]

for c in channel:
    GPIO.setup(c, GPIO.OUT)

red_pwm = GPIO.PWM(12, 100)  # 100Hz frequency
green_pwm = GPIO.PWM(13, 100)
blue_pwm = GPIO.PWM(19, 100)

for i in red_pwm , green_pwm, blue_pwm:
    i.start(0)

n=0

try:

        for r in range(100, 0, -5): #use -1 for 16.6 million colours
            red_pwm.ChangeDutyCycle(r)

            for g in range(100, 0, -5):
                green_pwm.ChangeDutyCycle(g )

                for b in range(100, 0, -5):
                    blue_pwm.ChangeDutyCycle(b)
                    sleep(0.05)
                    n=n+1
                    print("Total no.of colours::",n, "-- red=",r,", green=", g, ", blue=", b)

    
except KeyboardInterrupt:
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()

