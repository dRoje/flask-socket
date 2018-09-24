# Created by Duje 
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledPin = 27
GPIO.setup(ledPin, GPIO.OUT)

while True:
    GPIO.output(ledPin, 1)
    time.sleep(1)
    GPIO.output(ledPin, 0)
    time.sleep(1)
