from . import app

from flask_socketio import SocketIO

socketio = SocketIO(app)
