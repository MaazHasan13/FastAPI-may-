from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
class User(BaseModel):
    name : str
    age  : int

app = FastAPI()

# #home route
# @app.get("/")
# def home():
#     return {"welcome to faast api "}

# #about route
# @app.get("/about")
# def about():
#     return{"message:this my about route"}

# @app.get("/user/{user_id}/{rollno}")
# def get_user(user_id,rollno):
#     return {"user_id": user_id,"rollno":rollno}

# @app.get("/product")
# def get_product(limits : int = 10):
#     return {"limit" : limits}


# @app.post("/user_created")         #take only single user 
# def new_user(user: User):
#     return{
#         "message":"User created", #harded coded message
#         "data" : User
#     }


@app.post("/user_created")          #taking multiple user at a time
def new_user_first(user: List[User]):
    return{
        "message":"User created", #harded coded message
        "data" : user
    }


