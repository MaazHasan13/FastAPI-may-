from fastapi import FastAPI


app = FastAPI()

#home route
@app.get("/")
def home():
    return {"welcome to faast api "}

#about route
@app.get("/about")
def about():
    return{"message:this my about route"}

@app.get("/user/{user_id}/{rollno}")
def get_user(user_id,rollno):
    return {"user_id": user_id,"rollno":rollno}

@app.get("/product")
def get_product(limits : int = 10):
    return {"limit" : limits}