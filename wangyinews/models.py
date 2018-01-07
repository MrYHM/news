#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-06,14:55"
from . import db
import pymysql
pymysql.install_as_MySQLdb()

class News(db.Model):
    __tablename__ = "news"

    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(30),nullable = False)
    content = db.Column(db.Text,nullable = False)
    types = db.Column(db.String(20),nullable = False)
    image = db.Column(db.String(300))
    author = db.Column(db.String(20))
    view_count = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)

    def __repr__(self):
        return self.title

