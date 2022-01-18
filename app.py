from distutils.log import debug
from flask import Flask, render_template
from flask_mongoengine import MongoEngine
server = Flask(__name__)
server.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(server)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()

User(name='Chris', email='chris@gmail.com').save()

@server.route('/')
def index():
    return render_template('index.html', user='Christian')

if __name__ == '__main__':
    server.run(host='0.0.0.0', debug=True, port=3000)
