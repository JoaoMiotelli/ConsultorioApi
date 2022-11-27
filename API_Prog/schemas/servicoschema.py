from pydantic import BaseModel, validator
from datetime import datetime,date

class ServicoBase(BaseModel):
    id: int
    tipo_servico: int
    agendamento: int


class ServicoRequest(ServicoBase):
    ...

class ServicoResponse(ServicoBase):
    CPF: int

    class Config:
        orm_mode = True

