from flask import request
from flask_restplus import Resource

from models.customers import CustomersModel
from schemas.customers import CustomersSchema

from server.instance import server

customers_ns = server.customers_ns

customer_schema = CustomersSchema()
customer_list_schema = CustomersSchema(many=True)


class Customers(Resource):

    def get(self, id):
        customers_data = CustomersModel.Find_by_id(id)
        if customers_data:
            return customer_schema.dump()