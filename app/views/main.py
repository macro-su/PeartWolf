from flask import Blueprint, render_template, redirect, url_for, flash, request, render_template_string

# 创建蓝本对象
main = Blueprint('main', __name__)


@main.route('/', methods=['get', 'post'])
def helloWorld():
    if request.method == 'GET':
        return 'get hello world！!'
    elif request.method == 'POST':
        return 'post hello world！!'
    else:
        return request.method


@main.route('/index')
def index():
    return render_template("index.html")


@main.route('/projects/')
def projects():
    return 'The project page'


@main.route('/about')
def about():
    return 'The about page'


@main.route('/json', methods=['post'])
def json():
    rs = request
    return rs
