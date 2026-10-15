
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{
        "message":"hello soumya"
    }

@app.get("/add")
def add(a:int,b:int):
    return{
        "result":a+b
    }
#now go to test_main.py file