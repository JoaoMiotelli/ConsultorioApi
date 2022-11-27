from flask import jsonify

from ma import ma
from db import db

from controllers.customers import Customers, customer_list_schema
from marshmallow import ValidationError

from server.instance import server

api = server.api
app = server.app


@app.before_first_request
def create_table():
    db.create_all()

@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

api.add_resource(Customers, '/books/<int:id>')
api.add_resource(customer_list_schema, '/books')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()