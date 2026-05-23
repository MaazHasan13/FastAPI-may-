from fastapi import FastAPI,Depends
from pydantic import BaseModel
from sqlalchemy.orm import  declarative_base,sessionmaker,Session
from sqlalchemy import create_engine , Column,String,Integer

app = FastAPI()

engine  = create_engine("sqlite:///employee.db")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

class Employee(Base):
    __tablename__ = "employee"

    emp_id = Column(Integer,primary_key=True,index=True)
    emp_name = Column(String)
    emp_salary = Column(Integer)
    emp_domain = Column(String)

Base.metadata.create_all(bind=engine)

class Employeeschema(BaseModel):
    emp_id:int
    emp_name: str
    emp_salary:int
    emp_domain:str

#post api
@app.post("/new_employee")
def create_emp(emp:Employeeschema):
    db = SessionLocal()

    new_employee = Employee(    #base class db
        emp_id = emp.emp_id,
        emp_name = emp.emp_name,
        emp_salary = emp.emp_salary,
        emp_domain = emp.emp_domain
     )
    db.add(new_employee)
    db.commit()

    return{
        "message" : "employee added successfully..."
    }
@app.get("/emp_data/{emp_id}")
def get_empinfo(emp_id: int):

    db = SessionLocal()

    employee = db.query(Employee).filter(Employee.emp_id == emp_id).first()

    if employee:

        return {
            "MESSAGE": "EMPLOYEE FOUND",
            "DATA": employee
        }

    return {
        "MESSAGE": "EMPLOYEE NOT FOUND"
    }