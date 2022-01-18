from flask import Flask
server = Flask(__name__)

@server.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=3000)
