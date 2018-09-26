# Created by Duje
import Adafruit_ADS1x15 as ADS
from utils.mapping import mapping


class Potentiometer:
    def __init__(self, adc: ADS, adcRange, myRange):
        self._adc = adc
        self._adcRange = adcRange
        self._myRange = myRange

    @property
    def resistance(self):
        adcRead = max(0, self._adc.read_adc(0))
        return int(mapping(adcRead, 0, self._adcRange, 0, self._myRange))


