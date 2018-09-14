from flask import Flask, render_template
from flask_socketio import SocketIO
import time
from threading import Thread
import RPi.GPIO as GPIO

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = 'secret!'
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = SocketIO(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@socketio.on('my event')
def handle_message(message):
    print('received message: ' + str(message))


@socketio.on('buttonPressed')
def handle_message():
    print('button pressed')
    data = 2
    socketio.emit("buttonData", data)


class FlaskThread(Thread):
    def run(self):
        socketio.run(app, host="0.0.0.0")


def turnOnLight():
    pass


def turnOffLight():
    pass


if __name__ == '__main__':
    f = FlaskThread()
    f.start()

    while True:
        # BLINK
        turnOnLight()
        time.sleep(1)
        turnOffLight()
        time.sleep(1)
