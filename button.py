import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
Channel = 27
#GPIO.setup(Channel, GPIO.IN)
GPIO.setup(Channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
	if(GPIO.input(Channel) == GPIO.HIGH):
		print("Button pressed..."+str(time.time()))
		time.sleep(0.1)