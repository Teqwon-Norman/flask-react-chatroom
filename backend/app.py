from flask import Flask, render_template, request, session, redirect, send_from_directory
from flask_socketio import join_room, leave_room, send, SocketIO
from string import ascii_uppercase

import random as rand

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdasf'
socketio = SocketIO(app)

@app.route('/', methods=["POST", "GET"])
def home():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    socketio.run(app, debug=True)