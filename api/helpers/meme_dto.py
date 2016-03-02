from api.model.meme import Meme

class MemeDTO:

    @staticmethod
    def to_json(meme):
        json = dict()
        json['keywords'] = meme.keywords
        json['image_url'] = meme.image_url
        return json

    @staticmethod
    def from_json(json):
        meme = Meme()

        if 'keywords' in json:
            meme.keywords = json['keywords']

        if 'image_url' in json:
            meme.image_url = json['image_url']

        return meme
