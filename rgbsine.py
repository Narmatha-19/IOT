import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)  # Red
GPIO.setup(13, GPIO.OUT)  # Green
GPIO.setup(19, GPIO.OUT)  # Blue

red_pwm = GPIO.PWM(12, 100)  # 100Hz frequency
green_pwm = GPIO.PWM(13, 100)
blue_pwm = GPIO.PWM(19, 100)

red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)
n=0

try:
    while True:
        for i in range(0, 360, 1):  # 0° to 360° for full cycle
            
            red = math.sin(i) *50 + 50
            green = math.sin(i + 120) *50 +50
            blue = math.sin(i + 240) *50 +50

            red_pwm.ChangeDutyCycle(red)
            green_pwm.ChangeDutyCycle(green)
            blue_pwm.ChangeDutyCycle(blue)
            time.sleep(0.10)  
            print("No. of colours=",n)
            n+=1

except KeyboardInterrupt:
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()