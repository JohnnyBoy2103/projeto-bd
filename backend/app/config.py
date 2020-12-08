# -*- coding: utf-8 -*-
class Config:
    SECRET_KEY = 'PCS-3643-2020-PCSJobs-Backend'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pcsjohnny123@localhost/pcsjobs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_ECHO = True
    