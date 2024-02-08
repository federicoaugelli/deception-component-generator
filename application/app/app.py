from flask import Flask, request, jsonify, redirect, url_for, session
from sqlalchemy import create_engine, select, insert, update, delete
from sqlalchemy import MetaData, Table, Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
import os
from datetime import timedelta
#from auth_decorator import login_required
from dotenv import load_dotenv

load_dotenv()


# App config
app = Flask(__name__)
# Session config
#app.secret_key = os.getenv("APP_SECRET_KEY")
#app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)


# oAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    access_token_url=os.getenv("ACCESS_TOKEN_URL"),
    access_token_params=None,
    authorize_url=os.getenv("AUTHORIZE_URL"),
    authorize_params=None,
    api_base_url=os.getenv("API_BASE_URL"),
    userinfo_endpoint=os.getenv("USERINFO_ENDPOINT"),  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'email profile'},
    server_metadata_url=os.getenv("SERVER_METADATA_URL")
)


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

metadata_obj = MetaData()

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

