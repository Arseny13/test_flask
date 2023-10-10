from main import app, socketio, db


with app.app_context():
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    socketio.run(app)
