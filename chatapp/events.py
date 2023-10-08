from flask import request, session
from flask_socketio import emit, join_room, leave_room, send

from .models import Room
from . import db
from .extensions import socketio

users = {}


@socketio.on("connect")
def connect(auth):
    """Запускатся при подключении?"""
    code = session.get('code')
    name = session.get('name')
    room = Room.search_code(code)
    if not code or not name:
        return
    if room is None:
        leave_room(code)
        return

    join_room(code)
    send({"name": name, "message": "has entered the room"}, to=code)
    room.members += 1
    db.session.add(room)
    db.session.commit()
    print(f'{name} joined room {code}')


@socketio.on("disconnect")
def disconnect():
    code = session.get('code')
    name = session.get('name')
    leave_room(code)
    room = Room.search_code(code)
    if room is not None:
        room.members -= 1
        db.session.add(room)
        db.session.commit()
        if room.members <= 0:
            db.session.delete(room)
            db.session.commit()

    send({"name": name, "message": "has left the room"}, to=code)
    print(f'{name} left room {code}')


@socketio.on("message")
def message(data):
    code = session.get("code")
    room = Room.search_code(code)
    if room is not None:
        return

    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    # rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")


@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True)
