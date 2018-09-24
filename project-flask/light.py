import RPi.GPIO as GPIO


class Light:
    def __init__(self, pin: int, gpio: GPIO):
        self._pin = pin
        self._gpio = gpio
        self._gpio.setup(pin, GPIO.OUT)
        self.turnOff()
        
    def turnOn(self):
        self._gpio.output(self._pin, True)

    def turnOff(self):
        self._gpio.output(self._pin, False)

 
