from flask import jsonify
from flask_restful import Resource, Api
from src.server.models import Book
from src.server.models import db


class HelloWorld(Resource):
    def get(self):
        # my_model = Book( 'test_name2', 'test_aurhor2', 1)
        # db.session.add(my_model)
        # db.session.commit()

        my_returned_book = Book.query.get(1)
        return jsonify(my_returned_book.as_dict())

def add_resource(app):
    api = Api(app)
    api.add_resource(HelloWorld, '/')