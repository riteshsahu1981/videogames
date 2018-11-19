#from flask import url_for, redirect
from restapi import app
from restapi.models import GamesApi
from flask_restful import reqparse, abort, Api, Resource
api = Api(app)
api.add_resource(GamesApi,'/api/v1.0/<method_name>/', '/api/v1.0/<method_name>/<limit>/')