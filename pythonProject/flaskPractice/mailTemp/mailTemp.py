# -*- coding: UTF-8 -*-
from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'honglichen75@gmail.com'
app.config["MAIL_PASSWORD"] = '******'
app.config["MAIL_USE_TSL"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)

app.route('/')
def index():
    msg = Message("hello",sender="honglichen75@gmail.com",recipients="123@gmail.com")
    msg.body="this is a test example"
    mail.send(msg)
    return "sent"
if __name__ == "__main__":
    app.run(debug=True)
