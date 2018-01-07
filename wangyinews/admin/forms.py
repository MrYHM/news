#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-06,16:23"
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SelectField
from wtforms import FileField
from wtforms import SubmitField
from wtforms.validators import Required
from flask_wtf.file import FileField, FileRequired, FileAllowed

from .. import photos


class AddForm(FlaskForm):
    title = StringField(label = "新闻名称:",validators = [Required(message = "新闻名称不能为空")],render_kw = {"placeholder":"请输入新闻名称"})
    content = TextAreaField(label = "新闻内容:",validators = [Required(message = "新闻内容不能为空")])
    types = SelectField(label = "新闻类型:",
                        choices = [("推荐","推荐"),("百家","百家"),("本地","本地"),("吐槽","吐槽")],
                        validators = [Required(message = "新闻类别不能为空")],render_kw = {"placeholder":"请输入新闻类别"})
    image = FileField(label = "新闻图片:",validators = [FileRequired(message = "文件未选择"),FileAllowed(photos,message = "只能上传图片")])

    submit = SubmitField("提交",render_kw = {"class":"btn-danger"})


