from flask import Blueprint, render_template, request, session, redirect, url_for

from .utils import rooms, generate_unique_code

main = Blueprint("main", __name__)


@main.route("/", methods=['POST', 'GET'])
def index():
    session.clear()
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        join = request.form.get('join', False)
        create = request.form.get('create', False)
        print(name, code, join, create)
        if not name:
            return render_template(
                'index.html',
                error='Please enter a name.',
                code=code, name=name
            )

        if join and not code:
            return render_template(
                'index.html',
                error='Please enter a code.',
                code=code, name=name
            )

        room = code
        if create is not False:
            room = generate_unique_code(4)
            rooms[room] = {'members': 0, 'message': []}
        elif code not in rooms:
            return render_template(
                'index.html', error='This room does not exis',
                code=code, name=name
            )

        session['room'] = room
        session['name'] = name
        return redirect(url_for('main.room'))
    return render_template('index.html')


@main.route("/room", methods=['POST', 'GET'])
def room():
    room = session.get('room')
    if room is None or session.get('name') is None or room not in rooms:
        return redirect(url_for('main.index'))
    return render_template('room.html', room=room)
