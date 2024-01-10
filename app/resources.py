from flask_restx import Resource, Namespace 

from .api_models import *
from .extensions import db 
#from .models import User

ns = Namespace('api')

@ns.route('/check')
class Check(Resource):
    def get(self):
        return {'status': 'ok'}
