from flask import Flask, Blueprint
from flask_restplus import Api

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.bleuprint = Blueprint('api',__name__,url_prefix='/api')
        self.api = Api(self.bleuprint, doc='/doc',title='Clinica odontologia')
        self.app.register_blueprint(self.bleuprint)


        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.customer_ns = self.customer_ns()

    def customer_ns(self, ):
        return self.api.namespace(name='Customers', description='Customer', path='/')
 
    def run(self, ):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )

server = Server()