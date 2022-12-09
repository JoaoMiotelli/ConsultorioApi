from pydantic import BaseModel, validator
from datetime import datetime

class AgendamentoBase(BaseModel):
    cpf: int 
    data: str
    hora:str
    Status: int 
    id: int
    servico: str
    valor: float

class AgendamentoRequestNoId(BaseModel):
    cpf: int 
    data: str
    hora: str
    servico: str
    valor: float

class AgendamentoRequest(AgendamentoBase):
    ...

class AgendamentoResponse(AgendamentoBase):
    cpf: int

    class Config:
        orm_mode = True

