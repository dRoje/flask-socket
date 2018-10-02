# Created by Duje
from dimmer import Dimmer
from multiprocessing import Value
from potentiometer import Potentiometer
from consumer import Consumer
from flaskThread import socketio
import time


class FakePotentiometer(Potentiometer):
    def __init__(self):
        self.fakeResistance = Value('i', 0)

    @property
    def resistance(self):
        return self.fakeResistance.value


class Demo:
    def __init__(self, consumer: Consumer):
        self._consumer = consumer
        self._fakePotentiometer = FakePotentiometer()

    def showMeWhatYouGot(self):
        dimmer = Dimmer(self._fakePotentiometer, self._consumer, 100)
        dimmer.start()
        self.upwardDimmmer()
        self.downwardDimmer()
        dimmer.terminate()
        dimmer.join()
        for x in range(3):
            self.flash()
        time.sleep(0.5)

    def upwardDimmmer(self):
        for x in range(100):
            value = x
            socketio.emit("sliderValue", value)
            self._fakePotentiometer.fakeResistance.value = value
            time.sleep(0.01)

    def downwardDimmer(self):
        for x in range(100):
            value = 100 - x
            socketio.emit("sliderValue", value)
            self._fakePotentiometer.fakeResistance.value = value
            time.sleep(0.01)

    def flash(self):
        self._consumer.turnOff()
        socketio.emit("sliderValue", 0)
        time.sleep(0.3)
        self._consumer.turnOn()
        socketio.emit("sliderValue", 100)
        time.sleep(0.1)
        self._consumer.turnOff()
        socketio.emit("sliderValue", 0)
