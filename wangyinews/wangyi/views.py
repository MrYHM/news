#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-06,15:55"
from flask import render_template
from . import main
from ..models import News

@main.route("/index",methods = ["GET","POST"],endpoint = "index")
def index():
    news_list = News.query.all()
    return render_template("index.html",news_list=news_list)

@main.route("/cat/<name>",endpoint = "cat")
def cat(name):
    return "hello"

@main.route("/detail/<int:pk>",endpoint = "detail")
def detail(pk):
    return "world"
