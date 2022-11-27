from pydantic import BaseModel, validator
from datetime import datetime,date

class CustomerBase(BaseModel):
    CPF: int 
    Name: str 
    Data_nascimento: date 
    Estado_civil: str 
    Sexo: str 

    @validator("Data_nascimento", pre=True)
    def parse_birthdate(cls, value):
        try:
            return datetime.strptime(
                value,
                "%d-%m-%Y"
            ).date()
        except:
            return value

class CustomerRequestNoId(BaseModel):
    Name: str 
    Data_nascimento: date
    Estado_civil: str 
    Sexo: str 

    @validator("Data_nascimento", pre=True)
    def parse_birthdate(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()

class CustomerRequest(CustomerBase):
    ...

class CustomerResponse(CustomerBase):
    CPF: int

    class Config:
        orm_mode = True

