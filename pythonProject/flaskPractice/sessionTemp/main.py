# -*- coding: UTF-8 -*-
from flask import Flask, session, redirect, request, url_for

app = Flask(__name__)
# flask应用程序需要一个定义的secret_key 用于对会话数据加密
app.secret_key = 'asdsdsdsdsdsdsda'


@app.route('/')
def index():
    if "username" in session:
        username = session["username"]
        return "logged in as "+username + " <br> <b> <a href='/logout'> log out </b> "
    return "登录失败<br><b><a href='/login'>log in</b>"


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return """
    <form action="" method="post">
    <p><input type="text" name="username"></p>
    <p><input type="submit" value="login"></p>
    </form>
    """


@app.route('/logout')
def logout():
    # 注销 释放会话变量
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
