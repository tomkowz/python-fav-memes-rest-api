import flask
import os
import uuid
from werkzeug import secure_filename

from api import app
from api.model.meme import Meme
from api.helpers.meme_dao import MemeDAO

class MemeUploader:

    @staticmethod
    def upload(file, keywords_string):
        filename = MemeUploader._save_file_to_uploads(file)
        if filename is not None:
            keywords = MemeUploader._prepare_keywords_from_string(keywords_string)
            return MemeUploader._insert_meme(keywords, filename)

        return False, None

    @staticmethod
    def _save_file_to_uploads(file):
        if file and MemeUploader._allowed_file(file.filename):
            # Save file
            original_filename = secure_filename(file.filename)
            ext = original_filename.split('.')[1]
            filename = str(uuid.uuid4()) + '.' + ext

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return filename
        return None

    @staticmethod
    def _allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

    @staticmethod
    def _prepare_keywords_from_string(keywords_string):
        keywords_list = keywords_string.split(',')
        cleaned_keywords = list()
        for keyword in keywords_list:
            cleaned_keywords.append(keyword.strip())
        return cleaned_keywords

    @staticmethod
    def _insert_meme(keywords, filename):
        meme = Meme()
        meme.keywords = keywords
        meme.image_url = filename
        return MemeDAO.insert(meme), meme
