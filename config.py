# coding: utf-8

from __future__ import print_function
from os import environ, path
#from apscheduler.schedulers.background import BackgroundScheduler
#from flask import Flask
#from flask_marshmallow import Marshmallow
#from flask_cors import CORS

#from src.insiktes import InsiktEsService
#from src.insiktsmtp import InsiktSmtpService
from claroflexdb import ClaroflexDbService

#HEADERS = {
#    'Access-Control-Allow-Origin': '*',
#    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
#    'Access-Control-Max-Age': 1000,
#    'Access-Control-Allow-Headers': 'origin, x-csrftoken, content-type, accept',
#}

#SCHED = BackgroundScheduler(timezone="UTC", daemon=True)
#SCHED.start()

#if environ.get("INSIKT_APP_SETTINGS") is None:
#    environ["INSIKT_APP_SETTINGS"] = "../config/default.app.cfg"


#app = Flask(__name__)
app.config.from_envvar('INSIKT_APP_SETTINGS')
#CORS(app)

#ma = Marshmallow(app)

db_service = ClaroflexDbService(app.config)
#es_service = InsiktEsService(app.config, db_service)
#smtp_service = InsiktSmtpService(app.config, db_service)
