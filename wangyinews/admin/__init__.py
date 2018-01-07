#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-06,16:24"
from flask import Blueprint

admin = Blueprint("admin",__name__)

from . import views