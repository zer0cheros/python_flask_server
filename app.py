from flask import Flask, render_template
server = Flask(__name__)

@server.route('/')
def index():
    return render_template('index')

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=3000)
