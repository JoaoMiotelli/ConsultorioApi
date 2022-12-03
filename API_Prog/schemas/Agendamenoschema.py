from pydantic import BaseModel, validator
from datetime import datetime

class AgendamentoBase(BaseModel):
    CPF: int 
    datahora: datetime
    status: int 
    id: int

    @validator("datahora", pre=True)
    def parse_birthdate(cls, value):
        try:
            return datetime.datetime.strptime(
                value,
                "%d-%m-%Y %H:%M:%S"
            )
        except:
            return value

class AgendamentoRequestNoId(BaseModel):
    CPF: int 
    datahora: datetime
    status: int 

    @validator("datahora", pre=True)
    def parse_birthdate(cls, value):
        try:
            return datetime.datetime.strptime(
                value,
                "%d-%m-%Y %H:%M:%S"
            )
        except:
            return value

class AgendamentoRequest(AgendamentoBase):
    ...

class AgendamentoResponse(AgendamentoBase):
    CPF: int

    class Config:
        orm_mode = True

