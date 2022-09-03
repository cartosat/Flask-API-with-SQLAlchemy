from flask_marshmallow import Marshmallow
from flask_restful import Api
from app import app

ma = Marshmallow(app)
api = Api(app)
