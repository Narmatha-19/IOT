import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)  # Red

red_pwm = GPIO.PWM(12, 100)
red_pwm.start(0)

try:
    while True:
        # Exponential fade in (slow to fast)
        for t in range(0, 101, 1):
            duty = t ** 2 / 100  # Quadratic easing
            red_pwm.ChangeDutyCycle(duty)
            time.sleep(0.01)

        # Exponential fade out (fast to slow)
        for t in range(100, -1, -1):
            duty = t ** 2 / 100
            red_pwm.ChangeDutyCycle(duty)
            time.sleep(0.01)

except KeyboardInterrupt:
    pass

finally:
    red_pwm.stop()
    GPIO.cleanup()