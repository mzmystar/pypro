# -*- coding: UTF-8 -*-
from flask import Flask,render_template,request
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("student.html")


@app.route("/enternew")
def new_student():
    return render_template("student.html")

@app.route("/addrec", methods=["GET","POST"])
def addrec():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            addr = request.form.get("add")
            city = request.form.get("city")
            pin = request.form.get("pin")

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("insert into students(name,addr,city,pin)values (?,?,?,?)",(name,addr,city,pin))
                con.commit()
                msg = "add successfully"
        except:
            con.rollback()
            msg = "error is occured"
        finally:
            return render_template("result.html",msg=msg)
            con.close()

@app.route("/list")
def list():
    con =  sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from  students")
    rows = cur.fetchall()
    return render_template("list.html",rows=rows)

if __name__ == "__main__":
    app.run(debug=True)