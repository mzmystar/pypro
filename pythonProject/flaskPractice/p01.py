# -*- coding: UTF-8 -*-
from flask import Flask, redirect, url_for, request, render_template


# 简单的flask 基础应用

app = Flask(__name__)


@app.route('/hello')
def hello():
    my_str = 'hello world'
    my_int = 20
    my_array = [1, 2, 3, 4, 5]
    my_dict = {"a": 1, "b": 2, "c": 3}
    return render_template('hello.html', my_str=my_str, my_dict=my_dict, my_int=my_int, my_array=my_array)


@app.route('/index')
def index():
    return redirect(url_for('hello'))


@app.route('/welcome/<name>')
def welcome(name):
    return 'hello %s' % name


if __name__ == '__main__':
    app.run(debug=True)
