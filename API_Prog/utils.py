from schemas.customerschema import CustomerRequestNoId
from fastapi import HTTPException, status
from datetime import datetime

def custumer_validate(customer: CustomerRequestNoId) -> HTTPException:
    if len(customer.CPF) != 11:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="CPF invalido"
        )
    try:
        int(customer.CPF)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="CPF contém caracteres alfabeticos" 
        )
    
    try:
        todate(customer.Data_nascimento)
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Formato de data incorreto. Utilizar padrão Brasileiro" 
        )

    if customer.Estado_civil not in ('S', 'V', 'C'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Estado civil invalido"
        )

    if customer.Sexo not in ('M', 'F'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Tipo de sexo invalido"
        )

def todate(date):
    _date = datetime.strptime(date, '%d-%m-%Y').date()

    return _date