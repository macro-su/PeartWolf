from flask import Flask, request, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
if os.environ.get('FLASK_ENV') == 'development':
    # Windows set FLASK_ENV=development
    app.config.from_object('Config.DevConfig')
else:
    app.config.from_object('Config.ProdConfig')
CORS(app, resources=r'/*')


@app.route('/', methods=['get', 'post'])
def helloWorld():
    if request.method == 'get':
        return 'get hello world！!'
    elif request.method == 'post':
        return 'post hello world！!'


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/user/<username>')
def userName(username):
    return 'User name is %s' % username


@app.route('/user/<int:age>')
def userAge(age):
    return 'User age is %d' % age


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/json', methods=['post'])
def json():
    rs = request
    return rs


if __name__ == '__main__':
    app.run(host=app.config['FLASK_HOST'], port=app.config['FLASK_PORT'], threaded=True)
