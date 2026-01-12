
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
channel = 17
GPIO.setup(channel, GPIO.OUT)

while True:
      print( "[] Led Turning On.....")
      GPIO.output(channel, GPIO.HIGH)
      sleep(1)

      print( "[] Led Turning Off")
      GPIO.output(channel, GPIO.LOW)
      sleep(1)
