# Created by Duje
from abc import abstractmethod, ABCMeta
from adc import Adc
from utils.mapping import mapping


class Potentiometer:
    RANGE = 100

    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def resistance(self) -> int:
        """:returns value 0-100"""
        pass


class AnalogPotentiometer(Potentiometer):
    def __init__(self, adc: Adc):
        self._adc = adc

    @property
    def resistance(self):
        adcRead = max(0, self._adc.readChannel(0))
        return int(mapping(adcRead, 0, self._adc.range, 0, self.RANGE))
