import os
import flask
import uuid
from werkzeug import secure_filename

from api import app
from api.model.meme import Meme
from api.helpers.meme_dao import MemeDAO
from api.helpers.meme_uploader import MemeUploader

@app.route('/')
def main():
    return flask.render_template('layout.html')

@app.route('/add_meme', methods=['GET'])
def add_meme_page():
    return flask.render_template('add_meme.html')

@app.route('/add_meme', methods=['POST'])
def add_meme_page_post():
    keywords_string = flask.request.form['keywords']
    file = flask.request.files['file']
    success, meme = MemeUploader.upload(file, keywords_string)
    if success == True:
        return flask.redirect(flask.url_for('main'))
    else:
        return 'Cannot upload file.'
