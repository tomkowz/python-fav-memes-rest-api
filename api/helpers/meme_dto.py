from api.model.meme import Meme

class MemeDTO:

    @staticmethod
    def to_json(meme):
        json = dict()
        json['keywords'] = meme.keywords
        json['filename'] = meme.filename
        return json

    @staticmethod
    def from_json(json):
        meme = Meme()

        if 'keywords' in json:
            meme.keywords = json['keywords']

        if 'filename' in json:
            meme.filename = json['filename']

        return meme
