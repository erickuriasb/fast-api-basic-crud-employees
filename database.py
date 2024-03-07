import models
import schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import update


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    """ Docstrings """
    return db.query(models.Employee).offset(skip).limit(limit).all()


def get_employee_by_id(db: Session, employee_id: int):
    """ Docstrings """
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    """ Docstrings """
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, employee_id: int, updated_employee: schemas.EmployeeUpdate):
    """ Docstrings """
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id).first()
    if not employee:
        return HTTPException(status_code=404, detail="Employee not found")
    stmt = update(models.Employee).where(models.Employee.id ==
                                         employee_id).values(position=updated_employee)
    db.execute(stmt)
    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(db: Session, employee_id: int):
    """ Docstrings """
    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id).first()
    if not employee:
        return HTTPException(status_code=404, detail="Employee not found")
    db.delete(employee)
    db.commit()
    return employee
