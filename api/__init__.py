import os
import sqlite3
import flask

app = flask.Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'resources/memes.db'),
    UPLOAD_FOLDER=os.path.join(app.root_path, 'uploads'),
    ALLOWED_EXTENSIONS = set(['jpg', 'png', 'gif', 'jpeg']),
    DEBUG=False,
    SECRET_KEY='dj399-4idcx-d9vbx-anbc9-39dmc'
))

from endpoints import memes, uploads
from front import common

@app.before_request
def before_request():
    flask.g.db = sqlite3.connect(app.config['DATABASE'])

@app.teardown_request
def teardown_request(exception):
    db = getattr(flask.g, 'db', None)
    if db is not None:
        db.close()
