import random
import string

from . import db
from .db import Room

rooms = {}


def generate_unique_code(length: int) -> str:
    """Generate code."""
    while True:
        code = ''
        for _ in range(length):
            code += random.choice(string.ascii_uppercase)

        if Room.query.filter_by(code=code).first() is None:
            room = Room(code=code)
            db.session.add(room)
            db.session.commit()
            break

    return code
