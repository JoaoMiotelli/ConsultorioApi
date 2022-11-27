from ma import ma 
from models.customers import CustomersModel

class CustomersSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CustomersModel
        load_instance = True