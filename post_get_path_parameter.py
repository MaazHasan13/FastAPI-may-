from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#temp database
stu_data = []


#schema 
class Student(BaseModel):
    name:str
    roll_no: int
    course:str

#postapi

@app.post("/student")
def create_stu(student:Student):       #requset body
    stu_data.append(student.dict())
    return{
        "DATA" : student
    }

#getapi

@app.get("/get_stu/{roll_NO}")
def get_stu(roll_no:int):
    for student in stu_data:
        if student["roll_no"] == roll_no:
            return {
                "MESSAGE": "STUDENT INFORMATION",
                "DATA": student
            }

    return {
        "MESSAGE": "Student Not Found"
    }
#scema for employee
class Employee(BaseModel):
    emp_name : str
    emp_salary : int 
    emp_work :str 
    

#temp db for emp
emp_data = []
#api
@app.post("/employee")
def create_emp(emp:Employee):
    emp_data.append(emp)
    return{
        "message":"data added to the list",
        "DATA":emp_data
    }

#get api for employee
@app.get("/emp/{emp_name}")
def get_data(emp_name:str):
    for temp in emp_data:
        if temp.emp_name == emp_name :
            return{
                "message": "employee found",
                "detail" : temp 
            }
        
        
        else:
            return{
                "message":"emp not found"
            }
