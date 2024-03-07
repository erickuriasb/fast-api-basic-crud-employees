from typing import Optional
from pydantic import BaseModel


class EmployeeBase(BaseModel):
    name: str
    position: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    position: str

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True