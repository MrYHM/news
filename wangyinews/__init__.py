#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2018-01-06,15:56"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)


def create_app():
    app = Flask(__name__)
    app.config.from_object (Config)
    db.init_app(app)
    bootstrap.init_app(app)
    Config.init_app(app)
    configure_uploads (app,photos)
    patch_request_class(app)
    from .wangyi import main
    app.register_blueprint(main)
    from .admin import admin
    app.register_blueprint(admin,url_prefix="/admin")
    return app