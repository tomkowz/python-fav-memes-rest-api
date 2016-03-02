import flask
import uuid
import os

from api import app

@app.route('/api/uploads/<filename>', methods=['GET'])
def get_file(filename):
    upload_dir = app.config['UPLOAD_FOLDER']
    full_path = os.path.join(upload_dir, filename)
    if os.path.isfile(full_path) == True:
        return flask.send_from_directory(upload_dir, filename), 200
    return flask.jsonify({'message': 'File not found'}), 400
