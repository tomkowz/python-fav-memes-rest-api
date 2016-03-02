# python-fav-memes-rest-api
RESTful Web Service written in Python/Flask for storing and getting your favourite memes

### Motivation
I created this simple Restful service to learn how to build restful service in Python using [Flask](http://flask.pocoo.org) microframework.

The service allows you to store your favourite memes, access them via object id, as well as filtering with phrase that searches through keywords associated with memes.

### Files

- *paw.paw* - List of available requests to do via [Paw](https://luckymarmot.com/paw) app.
- *recreate_db* - shell script that removed database and create another one.
- *run.py* - use to run the service.

### Endpoints
- GET /memes
- GET /memes/id
- POST /memes
- POST /memes/search
- GET /uploads/filename

### Run
`python run.py`

### Frontend
API contains some frontend that you can use to upload your favourite memes (`api/front/common.py`).
However, the purpose of this project was to create fully functional rest service. Frontend is just a small addition.

### License
MIT
