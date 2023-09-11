# -*- coding: UTF-8 -*-
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, RadioField, SelectField, \
    IntegerField, validators, ValidationError


class ContactForm(Form):
    name = StringField("name of TextField", [validators.InputRequired("your name")])
    gender = RadioField("gender ", choices=[('M', "male"), ("F", "female")])
    address = TextAreaField("address")
    email = StringField("email", [validators.InputRequired("input your email"), validators.Email("input your email")])
    age = IntegerField("age")
    language = SelectField("language", choices=[("c++", "C&plus&plus"), ("py", "python")])
    submit = SubmitField("submit")
