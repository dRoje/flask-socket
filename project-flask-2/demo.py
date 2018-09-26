# Created by Duje
from potentiometer import Potentiometer
from dimmer import Dimmer
from flaskThread import socketio
import time


class Demo:
    def __init__(self, potentiometer: Potentiometer, dimmer: Dimmer):
        self._potentiometer = potentiometer
        self._dimmer = dimmer

    def showMeWhatYouGot(self):
        self.upwardDimmmer()
        self.downwardDimmer()
        for x in range(3):
            self.flash()
        time.sleep(0.5)

    def upwardDimmmer(self):
        for x in range(100):
            value = x
            socketio.emit("sliderValue", value)
            self._dimmer.volume = int(value / 100 * self._dimmer.range)
            time.sleep(0.01)

    def downwardDimmer(self):
        for x in range(100):
            value = 100 - x
            socketio.emit("sliderValue", value)
            self._dimmer.volume = int(value / 100 * self._dimmer.range)
            time.sleep(0.01)

    def flash(self):
        self._dimmer.volume = 0
        socketio.emit("sliderValue", self._dimmer.volume)
        time.sleep(0.3)
        self._dimmer.volume = self._dimmer.range
        socketio.emit("sliderValue", self._dimmer.volume)
        time.sleep(0.1)
        self._dimmer.volume = 0
        socketio.emit("sliderValue", self._dimmer.volume)