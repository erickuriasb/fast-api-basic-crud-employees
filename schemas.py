from typing import Optional
from pydantic import BaseModel


class EmployeeBase(BaseModel):
    name: str
    position: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    id: Optional[int]

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True