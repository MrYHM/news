#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-06,16:25"
import datetime

from flask import render_template,redirect,url_for,request
from .forms import AddForm
from . import admin
from ..models import News
from .. import photos
from .. import db



@admin.route("/add",methods = ["GET","POST"],endpoint = "add")
def add_news():
    form = AddForm()
    if form.validate_on_submit():
        filename = photos.save(form.image.data)
        file_url = photos.url(filename)
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.types = form.types.data
        news.image = file_url
        news.create_date = datetime.datetime.now()
        db.session.merge(news)
        db.session.commit()
        return redirect(url_for("admin.news_list"))
    else:
        file_url = None

    return render_template('admin/add.html',form=form,file_url = file_url)

@admin.route("/list",endpoint = "news_list")
@admin.route("/list/<int:page>")
def news_list(page=None):
    if not page:
        page = 1
    news_list = News.query.paginate(page=page,per_page = 5)
    return render_template("admin/news_list.html",news_list = news_list)

@admin.route("/delete/<int:nid>",endpoint = "delete")
def delete(nid):
    delete_new = News.query.filter_by(id=nid).first()
    db.session.delete(delete_new)
    db.session.commit()
    return redirect(url_for("admin.news_list"))

@admin.route("/edit/<int:nid>",endpoint = "edit",methods = ["GET","POST"])
def edit(nid):
    edit_new = News.query.filter_by(id=nid).first()
    form = AddForm(title = edit_new.title,content = edit_new.content,types = edit_new.types,image = edit_new.image)
    if form.validate_on_submit():
        filename = photos.save (form.image.data)
        file_url = photos.url(filename)
        news = News()
        news.id = int(nid)
        news.title = form.title.data
        news.content = form.content.data
        news.types = form.types.data
        news.image = file_url
        db.session.merge(news)
        db.session.commit()
        return redirect(url_for("admin.news_list"))
    return render_template("admin/add.html",form=form)
