# Created by Duje 
from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread
import logging

app = Flask(__name__, static_folder="static", template_folder="templates")
socketio = SocketIO(app)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route("/")
def home():
    return render_template('home.html')


@socketio.on('connection')
def connection(message):
    print('Connection established: ' + str(message))


class FlaskThread(Thread):
    def run(self):
        socketio.run(app, host="0.0.0.0")
