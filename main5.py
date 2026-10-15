from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     email:str
    
# @app.post("/create-user")
# def create_user(user:User):
#     return{
#         "message":"User created",
#         "data":user
#     }


#nested models
class Address(BaseModel):
    city:str
    pin:int
class User(BaseModel):
    name:str
    age:int
    address:Address # link by using Address
    
@app.post("/create-user")
def create_user(user:User):
    return user