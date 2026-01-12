import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
channel = [12, 13, 19]

for c in channel:
	GPIO.setup(c, GPIO.OUT)

x = [0,1,2,3,4,5,6,7,8]

for c in channel:
	p = GPIO.PWM( c ,2)
	p.start(100)
    
try:
	while True:
	    for i in x:
	    	rgb = format(i,'03b')
			
			for i, c in enumerate(channel):
	    		print(i,c,rgb[i])
				
				for dc in range(0, 101, 5):
					p.ChangeDutyCycle(dc)
                    time.sleep(0.1)
                    GPIO.output(c, bool(int(rgb[i])))
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
	print("Quitting....")# my try to glow multiple colours using rgb led
