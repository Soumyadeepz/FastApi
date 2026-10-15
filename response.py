from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel): # response model use kore amra sensitive data hide kore pathai
    name:str
    age:int
    
@app.get("/user",response_model=UserResponse) # response model jai data gula ache user sudhu seguloi dakhte pabe 
def get_user():
    return{
        "name":"mohit",
        "age" : 24,
        "password":"12345"
    }