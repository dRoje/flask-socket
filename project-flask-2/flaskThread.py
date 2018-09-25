# Created by Duje 
from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread
import logging
from slider import Slider

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = 'secret!'
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = SocketIO(app)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@socketio.on('connection')
def connection(message):
    print('Connection established: ' + str(message))


@socketio.on('demo')
def demo():
    print("DEMO")
    Slider.demo = True


class FlaskThread(Thread):
    def run(self):
        socketio.run(app, host="0.0.0.0")
