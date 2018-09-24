# Created by Duje
import Adafruit_ADS1x15 as ADS


class Potentiometer:
    def __init__(self, adc : ADS):
        self._adc = adc

    @property
    def resistance(self):
        return max(0, self._adc.read_adc(0))



