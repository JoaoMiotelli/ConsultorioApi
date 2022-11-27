from db import db
from typing import List

class CustomersModel(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Data_nascimento = db.Column(db.Date, nullabe=False)
    CPF = db.Column(db.String(11), nullable=False, unique=True)
    Estado_civil = db.Column(db.String(1), nullable=False)
    Sexo = db.Column(db.String(1), nullable=False)

    def __init__(self, Name, Data_nascimento, CPF, Estado_civil, Sexo):
        self.CPF = CPF
        self.Data_nascimento = Data_nascimento
        self.Estado_civil = Estado_civil
        self.Sexo = Sexo
        self.Name = Name

    def __repr__(self, ):
        return f'CustomersModel(Name={self.Name}, Data_nascimento={self.Data_nascimento}, CPF={self.CPF}, Estado_civil={self.Estado_civil}, Sexo={self.Sexo})'

    def json(self, ):
        return {
                'Name': self.Name, 
                'Data_nascimento': self.Data_nascimento, 
                'CPF': self.CPF, 
                'Estado_civil': self.Estado_civil, 
                'Sexo': self.Sexo
            }

    @classmethod
    def Find_by_cpf(cls, _CPF) -> "CustomersModel":
        return cls.query.filter_by(CPF=_CPF).first()

    @classmethod
    def Find_by_id(cls, _id) -> "CustomersModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def Find_all(cls) -> List["CustomersModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()