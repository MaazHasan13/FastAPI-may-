from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


Todos = []

class Todo(BaseModel):
    id : int
    title : str
    completed : bool    

@app.post("/todos")
def create_todo(todo:Todo):
    Todos.append(todo)
    return {"message" : "TODO added","Data ":todo}


@app.get("/todos")
def get_info():
    return{
        "meassage " : "list of data",
        "data" : Todos
    }