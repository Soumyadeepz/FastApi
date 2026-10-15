from fastapi import FastAPI,Depends,Header,HTTPException

app = FastAPI()

# process -1
def common_logic():
    return {
        "message":"Common Logic executed"
    }
@app.get("/home")
def home(data=Depends(common_logic)): # common_logic function ta amra depends ar moddha wrap korchi
    return data

# process -2
# reusable logic and function 
def get_current_user():
    return {
        "user":"Mohit"
    }
@app.get("/profile")
def profile(user= Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(user = Depends(get_current_user)):
    return user

# auth ...
# token header a thake so header import kore nibo

def verify_token(token: str=Header(None)): #token pabo str a jata initially null
    
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return{
        "user":"Authorized user"
    }
    
@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return {
        "message":"Secure data accessed",
        "user": user
    }