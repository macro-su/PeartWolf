from flask import Blueprint, render_template, redirect, url_for, flash, request, render_template_string

# 创建蓝本对象
user = Blueprint('user', __name__)


@user.route('/<username>')
def userName(username):
    return 'User name is %s' % username


@user.route('/<int:age>')
def userAge(age):
    return 'User age is %d' % age

