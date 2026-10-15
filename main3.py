#dynamic routes

from fastapi import FastAPI
app = FastAPI()

#users route

@app.get("/users/{user_id}")# dynhamically we pass user_id ..
def get_user(user_id:int):
    return {"user_id":user_id}

#query parameter

#/users?name = mohit
#/products?price=1000 ---- price =1000,name = mohit ai value gula query parameter diya handle kora hoi

@app.get("/user") # http://127.0.0.1:8000/user?name=mohit
def get_users(name: str=None): # if there are no name return null
    return {"name":name}

# default values
@app.get("/products")
def get_users(limit: int = 10): # by default limit =10
    return {"limit":limit}

@app.get("/items")#http://127.0.0.1:8000/items?name=laptop&price=200
def get_users(name: str = None,price : int =0): 
    return {
        "name":name,
        "price":price
    }