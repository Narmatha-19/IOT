"""import RPi.GPIO as GPIO

channel = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)

p = GPIO.PWM(channel,0.5)
p.start(100)
i =  None

try:
    while i != 'q':

        try:
            d = input("Set a duty cycle:")
            f = input("Set a frequency:")

            if(d  == 'q' or f == 'q'):

               break

            p.ChangeDutyCycle(int(d))
            p.ChangeFrequency(int(f))

        except ValueError as a:
            pass

except KeyboardInterrupt as e:
    print("Received Ctrl+C -> Quitting.....")


p.stop()
GPIO.cleanup()
print("I am exiting..")"""
#---------------------------------

import time    #sibi code
import RPi.GPIO as GPIO
channel = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

p = GPIO.PWM(channel, 60) #channel = 12 frequency = 50 HZ
print("Starting PWM")
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        for dc in range(100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()# I didnot get the output . watch the doubt session pwmrgb for this.