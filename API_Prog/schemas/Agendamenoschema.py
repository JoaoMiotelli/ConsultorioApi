from pydantic import BaseModel, validator
from datetime import datetime

class AgendamentoBase(BaseModel):
    cpf: int 
    data: str
    hora:str
    Status: int 
    id: int

class AgendamentoRequestNoId(BaseModel):
    cpf: int 
    data: str
    hora: str
    Status: int 

class AgendamentoRequest(AgendamentoBase):
    ...

class AgendamentoResponse(AgendamentoBase):
    cpf: int

    class Config:
        orm_mode = True

