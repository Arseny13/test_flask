from . import db


class Room(db.Model):
    """Класс комнат."""
    __tablename__ = 'room'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(4), unique=True, nullable=False)
