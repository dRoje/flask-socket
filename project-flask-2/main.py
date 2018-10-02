from flaskThread import FlaskThread, socketio
import time
from consumer import Consumer
from adc import Ads1115
from dimmer import Dimmer
import RPi.GPIO as GPIO
from potentiometer import AnalogPotentiometer
from demo import Demo
from messenger import Messenger

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledPin = 27

adc = Ads1115(address=0x48, busNumber=1, range=32767)
light = Consumer(ledPin, GPIO)  # consumer can be reused for other purposes (fan, etc.) - Scalability
potentiometer = AnalogPotentiometer(adc)  # tie classes to interfaces (potentiometer -> adc) - Modularity (change adc easily)
dimmer = Dimmer(potentiometer, light, range=100)
dimmer.start()
demo = Demo(light)
f = FlaskThread()
f.start()

while True:
    if Messenger.message == "demo":
        dimmer.pause.value = True
        demo.showMeWhatYouGot()
        Messenger.message = ""
        dimmer.pause.value = False
    # socketio.emit("sliderValue", potentiometer.resistance) # DON'T do this! Avoid two processes accessing the same source (ADC in this case)
    socketio.emit("sliderValue", dimmer.volume)

    time.sleep(0.1)
