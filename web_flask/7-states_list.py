#!/usr/bin/python3
''' This starts a Flask web app '''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    ''' Removes the SQLAlchemy section '''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' Show HTML with list of states '''
    state_list = storage.all(State).values()
    return render_template('7-states_list.html', states=state_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
