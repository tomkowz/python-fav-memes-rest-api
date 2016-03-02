import flask

from api.model.meme import Meme

class MemeDAO:

    @staticmethod
    def get_all():
        cursor = flask.g.db.execute('select keywords, image_url from memes order by id desc')
        return MemeDAO.parse_rows(cursor.fetchall())

    @staticmethod
    def get_one(id):
        query_f = 'select keywords, image_url from memes where id={}'
        cursor = flask.g.db.execute(query_f.format(id))
        memes = MemeDAO.parse_rows(cursor.fetchall())
        if len(memes) == 1:
            return memes[0]
        else:
            None

    @staticmethod
    def insert(meme):
        if meme.keywords is None:
            print 'Meme keywords is None'
            return False

        if meme.image_url is None:
            print 'Meme image url is None'
            return False

        flask.g.db.execute('insert into memes (keywords, image_url) values (?, ?)',
            [','.join(meme.keywords), meme.image_url])
        flask.g.db.commit()
        return True

    @staticmethod
    def search(phrase):
        if phrase is None:
            return list()

        query_f = 'select keywords, image_url from memes where keywords like \'%{}%\''
        cursor = flask.g.db.execute(query_f.format(phrase))
        return MemeDAO.parse_rows(cursor.fetchall())

    @staticmethod
    def parse_rows(rows):
        memes = list()
        for row in rows:
            meme = Meme()
            meme.keywords = row[0].split(',')
            meme.image_url = row[1]
            memes.append(meme)

        return memes
