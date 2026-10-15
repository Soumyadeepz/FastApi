from fastapi import FastAPI
app = FastAPI()


# home route
@app.get("/")
def home():
    return {"message":"Welcome to Fastapi"}

# About Route 
@app.get("/about")
def about():
    return {"message":"Welcome to about page"}

#Users page
@app.get("/users")
def users():
    return{
        "users":["Mohit","Rohit","Amit"]
    }