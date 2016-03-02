import flask

from api import app
from api.model.meme import Meme
from api.helpers.meme_dao import MemeDAO
from api.helpers.meme_dto import MemeDTO
from api.helpers.meme_uploader import MemeUploader

@app.route('/api/memes', methods=['GET'])
def memes_get_all():
    memes = jsonify_memes(MemeDAO.get_all())
    return flask.jsonify({'memes': memes}), 200

@app.route('/api/memes', methods=['POST'])
def memes_add():
    keywords_string = flask.request.form['keywords']
    file = flask.request.files['file']
    success, meme = MemeUploader.upload(file, keywords_string)
    if success == True:
        return flask.jsonify({'meme': MemeDTO.to_json(meme)}), 201
    else:
        return flask.jsonify({'message': 'Upload failed'}), 400

@app.route('/api/memes/<id>', methods=['GET'])
def memes_get(id):
    meme = MemeDAO.get_one(id)
    if meme is not None:
        return flask.jsonify({'meme': MemeDTO.to_json(meme)}), 200
    else:
        return flask.jsonify({'message': 'Meme does not exist'}), 400

@app.route('/api/memes/search', methods=['POST'])
def memes_search():
    json = flask.request.get_json()
    if 'phrase' in json:
        filtered = MemeDAO.search(json['phrase'])
        memes = jsonify_memes(filtered)
        return flask.jsonify({'memes': memes}), 200

    return flask.jsonify({'message': 'Missing phrase'}), 400

def jsonify_memes(memes):
    if memes is None:
        return list()

    jsonified = list()
    for meme in memes:
        jsonified.append(MemeDTO.to_json(meme))
    return jsonified
