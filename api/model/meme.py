class Meme:

    def __init__(self):
        self._keywords = None
        self._filename = None

    @property
    def keywords(self):
        return self._keywords

    def keywords(self, v):
        self._keywords = v

    @property
    def filename(self):
        return self._filename

    def filename(self, v):
        self._filename = v
