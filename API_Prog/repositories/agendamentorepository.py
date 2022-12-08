from sqlalchemy.orm import Session
from models.ClassModels import AgendamentoModel

class AgendamentosRepository:
    @staticmethod
    def Find_by_id(db: Session, _id) -> "AgendamentoModel":
        return db.query(AgendamentoModel).filter(AgendamentoModel.id ==_id).first()

    @staticmethod
    def Find_by_cpf(db: Session, _cpf) -> "AgendamentoModel":
        return db.query(AgendamentoModel).filter(AgendamentoModel.cpf ==_cpf).all()

    @staticmethod
    def Exist_by_id(db: Session, _id) -> "AgendamentoModel":
        return db.query(AgendamentoModel).filter(AgendamentoModel.id ==_id).first() is not None

    @staticmethod
    def Exist_by_data(db: Session, data) -> "AgendamentoModel":
        return db.query(AgendamentoModel).filter(AgendamentoModel.data == data).first() is not None

    @staticmethod
    def Exist_by_hora(db: Session, hora) -> "AgendamentoModel":
        return db.query(AgendamentoModel).filter(AgendamentoModel.hora == hora).first() is not None

    @staticmethod
    def Find_all(db: Session) -> list["AgendamentoModel"]:
        return db.query(AgendamentoModel).all()

    @staticmethod
    def save_to_db(db: Session, agendamento: AgendamentoModel) -> "AgendamentoModel":
        db.add(agendamento)
        db.commit()
        return agendamento
        
    @staticmethod
    def update_db(db: Session, agendamento: AgendamentoModel) -> "AgendamentoModel":
        if agendamento.id:
            db.merge(agendamento)
        db.commit()
        return agendamento

    @staticmethod
    def delete_from_db(db: Session, _CPF: int) -> None:
        agendamento = db.query(AgendamentoModel).filter(AgendamentoModel.CPF ==_CPF).first()
        if agendamento is not None:
            db.delete(agendamento)
            db.commit()