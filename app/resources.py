from flask_restx import Resource, Namespace 

from .api_models import *
from .extensions import db 
#from .models import User

from .lang import *

ns = Namespace('api')

@ns.route('/check')
class Check(Resource):
    def get(self):
        return {'status': 'ok'}

# lista di endpoint da iterare (es. /user/.env)
endpoints = ['/prova1', '/prova2', '/user/.env']
for endpoint in endpoints:
    # per ora l'handler ritorna solo il nome dell'endpoint, qui si aggiunge la chiamata
    # all'LLM
    @ns.route(endpoint)
    class Handler(Resource):
        def get(self):
            return retreive_random_data(endpoint)
            