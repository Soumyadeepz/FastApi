#status code and responses

from fastapi import FastAPI,status,HTTPException, Request

from fastapi.responses import JSONResponse
app = FastAPI()

@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return{
        "message":"User created"
    }
    
# custom response
@app.get("/user")
def get_users():
    return{
        "status":"Success",
        "message":"Use Fetched",
        "data":{
            "name":"Soumya",
            "Age":24
        }
    }

# error handling 
@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404,
            detail="User Not Found"
        )
    return{
        "id":1,
        "name":"Mohit"
    }

# advance Exception handling 
#custom error
class UserNotFoundException(Exception):
    def __init__(self,name:str):
        self.name = name    

#global function
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request:Request,exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message":f"User {exc.name} not found "
        }
    )

@app.get("/user/{name}") # dynamically name nicchi
def get_user(name:str):
    if name != "mohit":
        raise UserNotFoundException(name)
    return {
        "name":name
    } 