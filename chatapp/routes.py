from flask import (
    Blueprint, render_template,
    request, session,
    redirect, url_for
)

from .models import Room

main = Blueprint("main", __name__)

rooms = {}


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
            room = Room.generate_room().code
        elif Room.search_code(code) is None:
            return render_template(
                'index.html', error='This room does not exis',
                code=code, name=name
            )

        session['code'] = room
        session['name'] = name
        return redirect(url_for('main.room'))
    return render_template('index.html')


@main.route("/room", methods=['POST', 'GET'])
def room():
    code = session.get('code')

    if (
        code is None or session.get('name') is None or
        Room.search_code(code) is None
    ):
        return redirect(url_for('main.index'))
    return render_template('room.html', code=code)
