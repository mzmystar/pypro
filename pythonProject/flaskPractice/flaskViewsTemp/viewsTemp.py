# -*- coding: UTF-8 -*-
from flask import render_template, Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask.views import View
app=Flask(__name__)
db=SQLAlchemy(app)
class User(db.Model):
    pass

class ListView(View):
    # 及插视图可以像常规函数一样用route()或更好的add_url_rule()附加到应用中
    # 当附加时，必须提供http方法的名称， 可用methods 属性承载

    methods = ["GET", "POST"]

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self) -> ft.ResponseReturnValue:
        if request.method == "POST":
            context = {"objects": self.get_objects()}
        return self.render_template(context)

class UserView(ListView):
    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return User.query.all()

class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name
    def dispatch_request(self) -> ft.ResponseReturnValue:
        return render_template(self.template_name)

# 使用类方法as_view() 将这个类转换到一个实际的视图函数，名称为传递的字符串
app.add_url_rule('/about', view_func=RenderTemplateView.as_view('about_page', template_name='about.html'))

# 工作方式：无论何时请求被调度，会创建这个类的一个新实例，并且dispatch_request()方法会以URL规则为参数调用
#             这个类本身会用传递到as_view()函数的参数来实例化