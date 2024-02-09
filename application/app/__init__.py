from flask import Flask
import os
from datetime import timedelta
from .extensions import api
from .resources import ns 
from dotenv import load_dotenv

def create_app():

    app = Flask(__name__)
    
    load_dotenv()


    app.secret_key = os.getenv("APP_SECRET_KEY")
    app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

    api.init_app(app)

    api.add_namespace(ns)
    #api.add_namespace(ns)
    #############################################

    return app
