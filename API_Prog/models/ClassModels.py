from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, Float
from datetime import datetime, date
from server.database import Base

class CustomersModel(Base):
    __tablename__ = "customers"

    CPF: int  = Column(Integer, primary_key=True)
    Name: str = Column(String(80), nullable=False)
    Data_nascimento: str = Column(String, nullable=False)
    Estado_civil: str  = Column(String(1), nullable=False)
    Sexo: str  = Column(String(1), nullable=False)

class AgendamentoModel(Base):
    __tablename__ = "Agendamento"

    id: int = Column(Integer, primary_key=True)
    data: str = Column(String, nullable=False)
    hora: str = Column(String, nullable=False)
    Status: int = Column(Integer, nullable=False, default=1)
    cpf: int = Column(Integer, ForeignKey("customers.CPF"), nullable=False)
    servico: str = Column(String, nullable=False)
    valor: float = Column(Float, nullable=False)

   

