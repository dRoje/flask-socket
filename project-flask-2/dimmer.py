# Created by Duje 
from light import Light
import time
from multiprocessing import Process, Value


class Dimmer(Process):
    def __init__(self, light: Light, range: int):
        Process.__init__(self)
        self._volume = Value('i', 0)
        self._frequency = 500
        self._light = light
        self.range = range

    def run(self):
        while True:
            dutyOn = self._volume.value / self.range
            dutyOff = 1 - dutyOn
            self._light.turnOn()
            time.sleep(dutyOn / self._frequency)
            self._light.turnOff()
            time.sleep(dutyOff / self._frequency)

    @property
    def volume(self):
        return self._volume.value

    @volume.setter
    def volume(self, volume: int):
        self._volume.value = volume
