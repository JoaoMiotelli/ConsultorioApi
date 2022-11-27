from sqlalchemy.orm import Session
from models.ClassModels import CustomersModel

class CustomersRepository:
    @staticmethod
    def Find_by_cpf(db: Session, _CPF) -> "CustomersModel":
        return db.query(CustomersModel).filter(CustomersModel.CPF ==_CPF).first()

    @staticmethod
    def Exist_by_cpf(db: Session, _CPF) -> "CustomersModel":
        return db.query(CustomersModel).filter(CustomersModel.CPF ==_CPF).first() is not None

    @staticmethod
    def Find_all(db: Session) -> list["CustomersModel"]:
        return db.query(CustomersModel).all()

    @staticmethod
    def save_to_db(db: Session, custumer: CustomersModel) -> "CustomersModel":
        db.add(custumer)
        db.commit()
        return custumer
        
    @staticmethod
    def update_db(db: Session, custumer: CustomersModel) -> "CustomersModel":
        if custumer.CPF:
            db.merge(custumer)
        db.commit()
        return custumer

    @staticmethod
    def delete_from_db(db: Session, _CPF: int) -> None:
        customer = db.query(CustomersModel).filter(CustomersModel.CPF ==_CPF).first()
        if customer is not None:
            db.delete(customer)
            db.commit()