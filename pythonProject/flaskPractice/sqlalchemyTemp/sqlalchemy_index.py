# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = 'random string'
app.template_folder = 'C:/Users/HG/PycharmProjects/pythonProject/flaskPractice/templates'

db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    addr = db.Column(db.String(100))
    pin = db.Column(db.String(100))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


@app.route("/")
def show_all():
    return render_template("show_all.html", students=Students.query.all())


@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        if not request.form["name"]:
            flash("please enter the name", "error")
        else:
            name = request.form["name"]
            city = request.form["city"]
            addr = request.form["addr"]
            pin = request.form["pin"]
            student = Students(name, city, addr, pin)
            db.session.add(student)
            db.session.commit()
            flash("record was successfully added")
            return redirect(url_for('show_all'))
    return render_template("new.html")


if __name__ == '__main__':
    # 耗时任务 避免后端卡死
    with app.app_context():
        db.create_all()
    app.run(debug=True)
