class Meme:

    def __init__(self):
        self._keywords = None
        self._image_url = None

    @property
    def keywords(self):
        return self._keywords

    def keywords(self, v):
        self._keywords = v

    @property
    def image_url(self):
        return self._image_url

    def image_url(self, v):
        self._image_url = v
