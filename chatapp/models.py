from __future__ import annotations
import random
import string

from . import db


class Room(db.Model):
    """Класс комнат."""
    __tablename__ = 'room'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(4), unique=True, nullable=False)
    members = db.Column(db.Integer,)

    @staticmethod
    def generate_room() -> Room:
        """Generate room."""
        while True:
            code = ''
            for _ in range(4):
                code += random.choice(string.ascii_uppercase)

            if Room.query.filter_by(code=code).first() is None:
                room = Room(code=code, members=0)
                db.session.add(room)
                db.session.commit()
                break

        return room

    @classmethod
    def search_code(self, code: str) -> Room:
        return self.query.filter_by(code=code).first()
