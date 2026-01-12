import RPi.GPIO as GPIO

channel = 19
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
print("I am exiting..")



#---------------------------------------------------------------------------

"""for i in [0,1,2,3,4,5,6,7,8]:
                rgb = format( i , '03b')
                for i, c in enumerate(channel):
                for d in [10,20,30,40,50,60,70,80,90,100]:
                    print(i, c, rgb[i])
                    GPIO.output(c, bool(int(rgb[i])))


for c in channel:
    p = GPIO.PWM( c ,2)

p.start(100)
x = [0,1,2,3,4,5,6,7,8]
try:
    while True:
        for i in x:
            rgb = format( i , '03b')
            for i, c in enumerate(channel):
                print(i, c, rgb[i])
                GPIO.output(c, bool(int(rgb[i])))

            

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    print("Quitting....")"""