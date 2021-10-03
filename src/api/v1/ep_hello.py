from flask_restx import (
    Namespace,
    Resource
)

api = Namespace('hello', 'Hello Functions')


@api.route('/')
class Hello(Resource):
    @api.doc('get')
    def get(self):
        return {'hello': 'world'}
