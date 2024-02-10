from flask_restx import Resource, Namespace 
#from .auth_decorator import login_required
from .api_models import *
#from .models import User
from flask import abort, redirect, url_for
from functools import wraps
from .lang import *
from .app import *
import os, json
from dotenv import load_dotenv
from .config import AppConfig
from .start import *

load_dotenv()
ns = Namespace('api')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)
        if user:
            return f(*args, **kwargs)
        return abort(403)
    return decorated_function


def create_handler(endpoint):
    @ns.route(endpoint)
    class Handler(Resource):
        @login_required
        def get(self):
            result = generate(endpoint)
            if os.getenv('SYNTAX_ADAPTION') == 'True':
                data = json.dumps(result)
                result = retreive_random_data(endpoint, data)
            #result = json.loads(result)
            return result



@ns.route('/check')
class Check(Resource):
    def get(self):
        return {'status': 'ok'}



for endpoint in AppConfig.endpoints:
    create_handler(endpoint)



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
