# Created by Duje 
from light import Light
from threading import Thread
import time
from multiprocessing import Process, Value


class Dimmer(Process):
    def __init__(self, light: Light, range: int):
        Process.__init__(self)
        self.val = Value('i', 0)
        self.frequency = 500
        self._light = light
        self._range = range

    def run(self):
        while True:
            dutyOn = self.val.value / self._range
            dutyOff = 1 - dutyOn
            self._light.turnOn()
            time.sleep(dutyOn / self.frequency)
            self._light.turnOff()
            time.sleep(dutyOff / self.frequency)
