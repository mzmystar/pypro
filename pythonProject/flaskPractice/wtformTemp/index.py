# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template, flash
from contactForm import ContactForm

app = Flask(__name__)
app.secret_key = "secret key"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == True:
            flash("all Fields are required")
            return render_template("contact.html", form=form)
        else:
            return render_template("success.html")
    elif request.method == "GET":
        return render_template("contact.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
