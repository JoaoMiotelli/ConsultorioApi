from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Float
from datetime import datetime, date
from server.database import Base

class CustomersModel(Base):
    __tablename__ = "customers"

    CPF: int  = Column(Integer, primary_key=True)
    Name: str = Column(String(80), nullable=False)
    Data_nascimento: date = Column(Date, nullable=False)
    Estado_civil: str  = Column(String(1), nullable=False)
    Sexo: str  = Column(String(1), nullable=False)

class AgendamentoModel(Base):
    __tablename__ = "Agendamento"

    id: int = Column(Integer, primary_key=True)
    datahora: datetime = Column(DateTime, nullable=False)
    Status: str = Column(String(1), nullable=False, default=1)
    cpf: int = Column(Integer, ForeignKey("customers.CPF"), nullable=False)


class servicoModel(Base):
    __tablename__ = 'servicos'

    id: int = Column(Integer, primary_key=True)
    tipo_servico: int = Column(Integer, ForeignKey("servicos_desc.id"),nullable=True)
    Agendamento: int = Column(Integer, ForeignKey("Agendamento.id"), nullable=False)

class servicoDescModel(Base):
    __tablename__ = 'servicos_desc'

    id: int = Column(Integer, primary_key=True)
    Descricao: str = Column(String(80), nullable=True)
    valor: float = Column(Float, nullable=False)

