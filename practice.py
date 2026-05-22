from fastapi import FastAPI

app = FastAPI()

#route
@app.get("/")
def info_route():
    return{
        "Message" : "working",
        "NAME":"MAAZ HASAn"
    }


@app.get("/page1")
def person_deatils():
    return{
        "name" : "maaz hasan",
        "id" : "098",
        "key" : "mnbpoi"
    }

@app.get("/student")
def stu_info():
    return{
        "Name":"Aditya tomoar",
        "Age" : 19,
        "Course" : "Btech"
    }
@app.get("/college")
def college():
    return{
        "COLLAEGE NAME" :"ALIGARH MUSLIM UNIVERSITY",
        "CITY" : "ALIGARH"
    }