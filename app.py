from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
#GET,POST,PUT,PATCH
class User(BaseModel):
    name:str
    age:int
    email:str
@app.post("/users")
def create_user(user:User):
    return {
        "message":"user created",
        "user":user
    }
@app.get("/")
def home():
    return {"message":"HEllo from api"}
@app.get("/contact")
def contact():
    return {"message":"Welcome to contact"}
#about,Test