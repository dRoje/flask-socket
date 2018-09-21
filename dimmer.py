# Created by Duje 
from light import Light
from threading import Thread
import time


class Dimmer(Thread):
    def __init__(self, light: Light, range: int):
        Thread.__init__(self)
        self.value = 0
        self.frequency = 100
        self._light = light
        self._range = range

    def run(self):
        while True:
            dutyOn = self.value / self._range
            dutyOff = 1 - dutyOn
            self._light.turnOn()
            time.sleep(dutyOn / self.frequency)
            self._light.turnOff()
            time.sleep(dutyOff / self.frequency)
