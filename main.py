from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from database import get_db
from models import Employee
from schemas import EmployeeCreate, EmployeeUpdate, Employee



app = FastAPI()

@app.get("/items/{item_id}")
def root(item_id: int):
    return {'item_id': item_id} 

