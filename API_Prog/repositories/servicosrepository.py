from sqlalchemy.orm import Session
from models.ClassModels import servicoModel

class CustomersRepository:
    @staticmethod
    def Find_by_id(db: Session, _id) -> "servicoModel":
        return db.query(servicoModel).filter(servicoModel.id ==_id).first()

    @staticmethod
    def Exist_by_id(db: Session, _id) -> "servicoModel":
        return db.query(servicoModel).filter(servicoModel.id ==_id).first() is not None

    @staticmethod
    def Find_all(db: Session) -> list["servicoModel"]:
        return db.query(servicoModel).all()

    @staticmethod
    def save_to_db(db: Session, servico: servicoModel) -> "servicoModel":
        db.add(servico)
        db.commit()
        return servico
        
    @staticmethod
    def update_db(db: Session, servico: servicoModel) -> "servicoModel":
        if servico.id:
            db.merge(servico)
        db.commit()
        return servico

    @staticmethod
    def delete_from_db(db: Session, _id: int) -> None:
        servico = db.query(servicoModel).filter(servicoModel.id ==_id).first()
        if servico is not None:
            db.delete(servico)
            db.commit()