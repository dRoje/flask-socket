# Created by Duje 
import Adafruit_ADS1x15 as ADS
from abc import abstractmethod, ABCMeta


class Adc:
    __metaclass__ = ABCMeta

    def __init__(self, range: int):
        self.range = range

    @abstractmethod
    def readChannel(self, channel: int) -> int:
        pass


class Ads1115(Adc):
    def __init__(self, address, busNumber, range):
        Adc.__init__(self, range)
        self.address = address
        self.busNumber = busNumber
        self._ads1115 = ADS.ADS1115(address=self.address, busnum=self.busNumber)

    def readChannel(self, channel: int):
        # robustness - expect things to fail
        try:
            return self._ads1115.read_adc(channel)
        except Exception as e:
            print(e)
            return 0
