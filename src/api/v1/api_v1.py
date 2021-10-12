from flask import Blueprint
from flask_restx import Api

from .ep_hello import api as ns_ep_hello


blueprint = Blueprint('Dev Ops Training', __name__, url_prefix='/api/v1')
api = Api(blueprint, title='Dev Ops Training Test3', version='V1.0', description='Dev Ops Training V1', )
api.add_namespace(ns_ep_hello)
