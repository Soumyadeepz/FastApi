
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

# validation using pydantic 
class User(BaseModel):
    name:str
    age:int

@app.post("/create-user")
def create_user(name:str,age:int):
    return{
        "name":name,
        "age":age
    }

# by using json input handling --we give multiple data in json in this format like name,mobile,age etc
#data validation is not happing ...data that are in dict is directly executed 
@app.post("/create-users")
def create_user(user:dict):
    return{
         "message":"User created successfully",
         "data":user
    }


# pydantic -- is used for validation 

@app.post("/creates-user")
def create_user(user:User):
    return{
         "message":"User created successfully",
         "data":user
    }