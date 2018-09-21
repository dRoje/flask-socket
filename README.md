# SETUP

### flask
- pip install flask-socketio

### ADS1115
- sudo apt-get update
- sudo apt-get install build-essential python-dev python-smbus python-pip
- sudo python3 -m  pip install adafruit-ads1x15
- sudo apt-get install -y i2c-tools

##### enable i2c conection
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
- sudo raspi-config