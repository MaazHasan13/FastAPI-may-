from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name : str
    roll_no : str
    course : str

#POST route

@app.post("/student")
def create_stu(student:Student):  #requst body
    return{
        "MESSEGE"  : "STUDETN CREATED",
        "DATA"  : student
    }
#schema
class Employee(BaseModel):
    name: str
    slaray :int 
    department : str

#post route
@app.post("/employee")
def create_employee(employee:Employee):
    return{
        "MESSAGE":"EMPLOYEE CREATED",
        "DATA" : employee
    }