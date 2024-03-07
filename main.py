from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from models import Employee
from schemas import Employee

from config import SessionLocal, engine
import database
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    """ Docstrings """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_message():
    """ Docstrings """
    return {"Message": "Hola Mundo!"}


@app.get("/employee/", response_model=List[schemas.Employee])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """ Docstrings """
    employees = database.get_employees(db, skip=skip, limit=limit)
    return employees


@app.get("/employee/{employee_id}/", response_model=schemas.Employee)
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    """ Docstrings """
    employee = database.get_employee_by_id(db=db, employee_id=employee_id)
    return employee


@app.post("/employee/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    """ Docstrings """
    employee = database.create_employee(db=db, employee=employee)
    return employee


@app.put("/employee/{employee_id}/", response_model=schemas.Employee)
def update_position_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    """ Docstrings """
    # import pdb; pdb.set_trace()
    employee = database.update_employee(
        db=db, employee_id=employee_id, updated_employee=employee.position)
    return employee


@app.delete("/employee/{employee_id}/", response_model=schemas.Employee)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """ Docstrings """
    employee = database.delete_employee(db=db, employee_id=employee_id)
    return employee
