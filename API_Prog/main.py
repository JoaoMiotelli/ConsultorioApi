from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models.ClassModels import *
from server.database import engine, Base, get_db
from repositories.customersrepository import CustomersRepository
from repositories.agendamentorepository import AgendamentosRepository
from repositories.servicosrepository import ServiceRepository
from schemas.customerschema import CustomerRequest, CustomerResponse, CustomerRequestNoId
from schemas.Agendamenoschema import AgendamentoRequest, AgendamentoResponse, AgendamentoRequestNoId
from schemas.servicoschema import ServicoRequest, ServicoResponse, ServicorequestNoId
from utils import *

Base.metadata.create_all(bind=engine)

app = FastAPI()


#Metodo Get retorna todos o clientes cadastrados
@app.get("/api/customer", response_model=list[CustomerResponse])
def find_all(db: Session = Depends(get_db)):
    customers = CustomersRepository.Find_all(db)
    return [CustomerResponse.from_orm(CustomersModel) for CustomersModel in customers]


#Metodo post para registrar um novo cliente
@app.post("/api/customer", response_model=CustomerRequest, status_code=status.HTTP_201_CREATED)
def create(request: CustomerRequest, db: Session = Depends(get_db)):
    validate = custumer_validate(request)
    if validate is None:
        customer = CustomersRepository.save_to_db(db, CustomersModel(**request.dict()))
        return CustomerResponse.from_orm(customer)
    else:  
        return validate

#Metodo get retorna o cliente pelo CPF
@app.get("/api/customer/{cpf}", response_model=CustomerResponse)
def find_by_cpf(cpf: int, db: Session = Depends(get_db)):
    customer = CustomersRepository.Find_by_cpf(db, cpf)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer não encontrado"
        )
    return CustomerResponse.from_orm(customer)

#Metodo delete apaga o cliente pelo ID
@app.delete("/api/customer/{cpf}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(cpf: int, db: Session = Depends(get_db)):
    if not CustomersRepository.Exist_by_cpf(db, cpf):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer não encontrado"
        )
    CustomersRepository.delete_from_db(db, cpf)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#Metodo put atualiza registro do cliente pelo ID
@app.put("/api/customer/{cpf}", response_model=AgendamentoResponse)
def update(cpf: int, request: CustomerRequest, db: Session = Depends(get_db)):
    if not CustomersRepository.Exist_by_cpf(db, cpf):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer não encontrado"
        )

    validate = custumer_validate(request)

    if validate is None:
        customer = CustomersRepository.update_db(db, CustomersModel(**request.dict()))
        return CustomerResponse.from_orm(customer)
    else:  
        return validate

#metodo retorna todas os agendamento
@app.get("/api/agendamento", response_model=list[AgendamentoResponse])
def find_all(db: Session = Depends(get_db)):
    customers = AgendamentosRepository.Find_all(db)
    return [AgendamentoResponse.from_orm(CustomersModel) for CustomersModel in customers]

#Metodo post para registrar um novo agendamento para o cliente
@app.post("/api/agendamento", response_model=AgendamentoRequestNoId, status_code=status.HTTP_201_CREATED)
def create(request: AgendamentoRequestNoId, db: Session = Depends(get_db)):
    if CustomersRepository.Exist_by_cpf(db, request.cpf):
        agendamento = AgendamentosRepository.save_to_db(db, AgendamentoModel(**request.dict()))
        return AgendamentoResponse.from_orm(agendamento)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer não encontrado"
        )

#Metodo get retorna o agendamento pelo CPF
@app.get("/api/agendamento/{cpf}", response_model=AgendamentoResponse)
def find_by_cpf(cpf: str, db: Session = Depends(get_db)):
    if CustomersRepository.Exist_by_cpf(db, cpf):
        agendamento = AgendamentosRepository.Find_by_cpf(db, cpf)
        return [AgendamentoResponse.from_orm(AgendamentoModel) for AgendamentoModel in agendamento]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer não encontrado"
        )

#Metodo put atualiza registro do agendamento pelo ID
@app.put("/api/agendamento/{id}", response_model=AgendamentoResponse)
def update(id: int, request: AgendamentoRequest, db: Session = Depends(get_db)):
    if not AgendamentoRequestNoId.Exist_by_cpf(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="customer não encontrado"
        )
    
    agendamento = AgendamentosRepository.update_db(db, AgendamentoModel(**request.dict()))
    return AgendamentoResponse.from_orm(agendamento)
