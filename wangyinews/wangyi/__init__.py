#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-06,14:54"
from flask import Blueprint


main = Blueprint("main",__name__)
from . import views