# Created by Duje
import Adafruit_ADS1x15 as ADS
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledPin = 27
adcAddress = 0x48
adcBusNumber = 1
adcRange = 32767
frequency = 500

GPIO.setup(ledPin, GPIO.OUT)
adc = ADS.ADS1115(address=adcAddress, busnum=adcBusNumber)

while True:
    adcRead = adc.read_adc(channel=0)
    dutyOn = adcRead / adcRange
    dutyOff = 1 - dutyOn
    GPIO.output(ledPin, 1)
    time.sleep(dutyOn / frequency)
    GPIO.output(ledPin, 0)
    time.sleep(dutyOff / frequency)
