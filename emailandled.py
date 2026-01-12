import smtplib
import RPi.GPIO as GPIO
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

Channel = 4
led = 17
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(Channel , GPIO.IN)
GPIO.setup(led , GPIO.OUT)

smtp_server = "smtp.gmail.com"
smpt_port = 587
sender_mail = "storageboxxweb@gmail.com"
sender_pass = "txhbpybptqlqxwmi"
receiver_mail = "itsammugi@gmail.com"

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_mail
    msg['To'] = receiver_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smpt_port)
        server.starttls()
        server.login(sender_mail, sender_pass)
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

try:
    while True:
        if GPIO.input(Channel):
            print("Motion detected! Sending email....")
            GPIO.output(led, GPIO.HIGH)
            print("LED_ON....")
            send_email(
                subject = "Motion Detected!..",
                body = "Hello Narmatha! \n Your Microwave rador sensor detected movement at home!..\n Take action Now..!"
            )
            time.sleep(0.5)
            GPIO.output(led, GPIO.LOW)
            time.sleep(0.5)
        else:
            GPIO.output(led ,GPIO.LOW)
            #print("Check the connectivity..")
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()



