from pydantic import BaseModel, validator
from datetime import datetime,date

class ServicoBase(BaseModel):
    id: int
    Agendamento: int
    Descricao: str
    valor: float

class ServicorequestNoId(BaseModel):
    Agendamento: int
    Descricao: str
    valor: float


class ServicoRequest(ServicoBase):
    ...

class ServicoResponse(ServicoBase):
    id: int

    class Config:
        orm_mode = True

