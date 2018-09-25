from flaskThread import FlaskThread, socketio
import time
from light import Light
import Adafruit_ADS1x15 as ADS
from dimmer import Dimmer
import RPi.GPIO as GPIO
from potentiometer import Potentiometer

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledPin = 27
adcAddress = 0x48
adcBusNumber = 1
adcRange = 32767
sliderRange = 100

adc = ADS.ADS1115(address=adcAddress, busnum=adcBusNumber)
potentiometer = Potentiometer(adc)
light = Light(ledPin, GPIO)
dimmer = Dimmer(light, adcRange)
dimmer.start()
f = FlaskThread()
f.start()

previousSliderValue = 0
while True:
    resistance = potentiometer.resistance
    sliderValue = int(resistance / adcRange * 100)
    if sliderValue != previousSliderValue:
        previousSliderValue = sliderValue
        socketio.emit("sliderValue", sliderValue)
        dimmer.value = resistance

    time.sleep(0.15)
