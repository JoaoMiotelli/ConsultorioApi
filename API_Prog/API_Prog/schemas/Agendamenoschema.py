from pydantic import BaseModel, validator
from datetime import datetime

class AgendamentoBase(BaseModel):
    CPF: int 
    datahora: str
    status: int 
    id: int

class AgendamentoRequestNoId(BaseModel):
    CPF: int 
    datahora: str
    status: int 

class AgendamentoRequest(AgendamentoBase):
    ...

class AgendamentoResponse(AgendamentoBase):
    CPF: int

    class Config:
        orm_mode = True

