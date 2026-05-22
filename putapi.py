from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#temp db
students = []

#schema
class Student(BaseModel):
    stu_name: str
    roll_num : int 
    course : str


#post api
@app.post("/student")
def create_stu(stu : Student):
    students.append(stu)
    return{
        "message":"student created",
        "data":stu
    }

#get api
@app.get("/get_stu/{roll_num}")
def info(roll_num:int):
    for i in students:
        if i.roll_num == roll_num:
            return {
                "message":"student found",
                "data" : i
            }
        
    return {

        "messagr " : "student not found"
    }
#put api
@app.put("/update/{roll_num}")
def update_stu(roll_num:int, update_stu:Student):
    for i in range(len(students)):
        if students[i].roll_num== roll_num:
            students[i]=update_stu
            return{
                "message":"student found",
                "update student" : students[i]
            }


    return{
        "messagr " : "student not found"
    }
#delete API
@app.delete("/delete_stu/{roll_no}")
def del_stu(roll_no:int):
    for i in range(len(students)):
        if students[i].roll_num == roll_no:
            delete_stu = students.pop(i)
            return{
                "Message":"student found",
                "data deleted" : delete_stu 
            }
        
    return{
        "message":"student not found."
    }
