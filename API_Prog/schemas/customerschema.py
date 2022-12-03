from pydantic import BaseModel, validator
from datetime import datetime,date

class CustomerBase(BaseModel):
    CPF: int 
    Name: str 
    Data_nascimento: str 
    Estado_civil: str 
    Sexo: str 

class CustomerRequestNoId(BaseModel):
    Name: str 
    Data_nascimento: str
    Estado_civil: str 
    Sexo: str 

class CustomerRequest(CustomerBase):
    ...

class CustomerResponse(CustomerBase):
    CPF: int

    class Config:
        orm_mode = True

