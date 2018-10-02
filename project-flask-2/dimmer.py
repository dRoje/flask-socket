# Created by Duje 
from consumer import Consumer
from potentiometer import Potentiometer
import time
from multiprocessing import Process, Value


class Dimmer(Process):
    def __init__(self, potentiometer: Potentiometer, consumer: Consumer, range: int):
        Process.__init__(self)
        self.pause = Value('i', False)
        self._volume = Value('i', 0)
        self._frequency = 500
        self._consumer = consumer
        self._potentiometer = potentiometer
        self.range = range

    def run(self):
        while True:
            if self.pause.value:
                continue
            self._volume.value = self._potentiometer.resistance
            dutyOn = self._volume.value / self.range
            dutyOff = 1 - dutyOn
            self._consumer.turnOn()
            time.sleep(dutyOn / self._frequency)
            self._consumer.turnOff()
            time.sleep(dutyOff / self._frequency)

    @property
    def volume(self):
        return self._volume.value

    @volume.setter
    def volume(self, volume: int):
        self._volume.value = volume
