# path+query+body combo
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# PUT /users/101?nitify =true
# {
#     "name":"Soumya"
#     "age":24
# }

users = []
class User(BaseModel):
    name :str
    age: int

@app.post("/users")
def create_user(user:User):
    users.append(user)
    return{
        "message":"user created",
        "data":user
    }

@app.put("users/{user_id}")
def updated_user(user_id:int,user:User,notify:bool=False):
    if user_id < len(users):
        users[user_id]= user
        return {
            "message":"User updated",
             "notify":notify,
             "data":user
        }
    return {
        "error":"user not found"
    }