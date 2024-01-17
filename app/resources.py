from flask_restx import Resource, Namespace 
#from .auth_decorator import login_required
from .api_models import *
from .extensions import db 
#from .models import User
from flask import abort, redirect, url_for
from functools import wraps
from .lang import *
from .app import *
import os
from dotenv import load_dotenv

load_dotenv()

ns = Namespace('api')

#app.secret_key = os.getenv("APP_SECRET_KEY")
#app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)
        if user:
            return f(*args, **kwargs)
        return abort(403)
    return decorated_function

@ns.route('/check')
class Check(Resource):
    def get(self):
        return {'status': 'ok'}


# lista di endpoint da iterare (es. /user/.env)
endpoints = ['/prova1', '/prova2', '/user/.env', '/user/data.xml']
for endpoint in endpoints:
    # per ora l'handler ritorna solo il nome dell'endpoint, qui si aggiunge la chiamata
    # all'LLM
    @ns.route(endpoint)
    class Handler(Resource):
        @login_required
        def get(self):
            return retreive_random_data(endpoint)


@ns.route('/login')
class Login(Resource):
    def get(self):
        google = oauth.create_client('google')  # create the google oauth client
        redirect_uri = url_for('api_authorize', _external=True)
        return google.authorize_redirect(redirect_uri)


@ns.route('/authorize')
class authorize(Resource):
    def get(self):
        google = oauth.create_client('google')  
        token = google.authorize_access_token()  
        #resp = google.get('userinfo')  
        #user_info = resp.json()
        user = oauth.google.userinfo()  
        session['profile'] = user
        session.permanent = True  
        return redirect('/api/check')


@ns.route('/logout')
class logout(Resource):
    @login_required
    def get(self):
        for key in list(session.keys()):
            session.pop(key)
        return redirect('/api/check')
