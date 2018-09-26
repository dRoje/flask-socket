from flaskThread import FlaskThread, socketio
from multiprocessing import Process, Value
import time
import Adafruit_ADS1x15 as ADS
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledPin = 27
adcAddress = 0x48
adcBusNumber = 1
adcRange = 32767
frequency = 500

GPIO.setup(ledPin, GPIO.OUT)
adc = ADS.ADS1115(address=adcAddress, busnum=adcBusNumber)

f = FlaskThread()
f.start()

adcRead = Value('i', 0)


def dimmer():
    while True:
        dutyOn = adcRead.value / adcRange
        dutyOff = 1 - dutyOn
        GPIO.output(ledPin, 1)
        time.sleep(dutyOn / frequency)
        GPIO.output(ledPin, 0)
        time.sleep(dutyOff / frequency)


p = Process(target=dimmer)
p.start()

while True:
    adcRead.value = adc.read_adc(channel=0)
    sliderValue = int(adcRead.value / adcRange * 100)
    socketio.emit("sliderValue", sliderValue)
    time.sleep(0.1)
