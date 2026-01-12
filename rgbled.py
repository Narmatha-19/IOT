import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
channel = [12, 13, 19]
#GPIO.setwarnings(False)
for c in channel:
	GPIO.setup(c, GPIO.OUT)

#GPIO.setup(channel, GPIO.OUT)

try:
	while True:
		try:
			i = input ("Enter a number between 0-7: ")
			i = int(i)
			if i < 0 or i >8:
				print("Invalid range of input... Try again.....!")
				continue

			rgb = format( i , '03b')
			for i, c in enumerate(channel):
				print(i, c, rgb[i])
				GPIO.output(c, bool(int(rgb[i])))

		except ValueError:
			print ("Invalid Input... Try again...!")

except KeyboardInterrupt:
	GPIO.cleanup()
	print("Quitting....")