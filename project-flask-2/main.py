from flaskThread import FlaskThread, socketio
import time
from light import Light
import Adafruit_ADS1x15 as ADS
from dimmer import Dimmer
import RPi.GPIO as GPIO
from potentiometer import Potentiometer
from demo import Demo
from messenger import Messenger

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledPin = 27
adcAddress = 0x48
adcBusNumber = 1
adcRange = 32767
sliderRange = 100

adc = ADS.ADS1115(address=adcAddress, busnum=adcBusNumber)
potentiometer = Potentiometer(adc, adcRange, sliderRange)
light = Light(ledPin, GPIO)
dimmer = Dimmer(light, sliderRange)
dimmer.start()
demo = Demo(potentiometer, dimmer)
f = FlaskThread()
f.start()

while True:
    if Messenger.message == "demo":
        demo.showMeWhatYouGot()
        Messenger.message = ""
    resistance = potentiometer.resistance
    socketio.emit("sliderValue", resistance)
    dimmer.volume = resistance

    time.sleep(0.1)
