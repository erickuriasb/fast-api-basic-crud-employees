from pydantic import BaseModel


class EmployeeBase(BaseModel):
    """ Docstrings """
    name: str
    position: str


class EmployeeCreate(EmployeeBase):
    """ Docstrings """
    pass


class EmployeeUpdate(BaseModel):
    """ Docstrings """
    position: str


class Employee(EmployeeBase):
    """ Docstrings """
    id: int

    class Config:
        """ Docstrings """
        orm_mode = True
