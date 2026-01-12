import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)  # Red
GPIO.setup(13, GPIO.OUT)  # Green (optional)
GPIO.setup(19, GPIO.OUT)  # Blue

red_pwm = GPIO.PWM(12, 100)
blue_pwm = GPIO.PWM(19, 100)

red_pwm.start(100)  # Start at full red
blue_pwm.start(0)   # Start at zero blue

try:
    while True:
        # Fade from red (100%) to blue (100%)
        for t in range(0, 101, 1):  # t = 0 to 100
            red = 100 - t           # Red decreases
            blue = t                # Blue increases
            red_pwm.ChangeDutyCycle(red)
            blue_pwm.ChangeDutyCycle(blue)
            time.sleep(0.02)

        # Fade back from blue to red
        for t in range(0, 101, 1):
            red = t
            blue = 100 - t
            red_pwm.ChangeDutyCycle(red)
            blue_pwm.ChangeDutyCycle(blue)
            time.sleep(0.02)

except KeyboardInterrupt:
    pass

finally:
    red_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()