from flaskThread import FlaskThread, socketio
import time
from light import Light
import Adafruit_ADS1x15 as ADS
from dimmer import Dimmer
import RPi.GPIO as GPIO
from potentiometer import Potentiometer
from slider import Slider

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledPin = 27
adcAddress = 0x48
adcBusNumber = 1
adcRange = 32767

adc = ADS.ADS1115(address=adcAddress, busnum=adcBusNumber)
potentiometer = Potentiometer(adc)
light = Light(ledPin, GPIO)
dimmer = Dimmer(light, adcRange)
dimmer.start()
f = FlaskThread()
f.start()

previousSliderValue = 0
while True:
    if Slider.demo is True:
        for x in range(100):
            Slider.value = x
            socketio.emit("sliderValue", Slider.value)
            dimmer.val.value = int(x / 100 * adcRange)
            time.sleep(0.05)
        Slider.demo = False
    else:
        resistance = potentiometer.resistance
        Slider.value = int(resistance / adcRange * Slider.range)
        if Slider.value != previousSliderValue:
            previousSliderValue = Slider.value
            socketio.emit("sliderValue", Slider.value)
            dimmer.val.value = resistance

        time.sleep(0.05)
