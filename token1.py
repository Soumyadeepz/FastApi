from fastapi import FastAPI,HTTPException,Depends,Header
from jose import jwt
from datetime import datetime,timedelta,timezone

app = FastAPI()

SECRET_KEY="mysecret"

ALGORITHM = "HS256" # algorithm to hash token

# create token
def create_token(data: dict):# token dict ar form a thakbe 
    to_encode = data.copy() # data copy kore rakhbo
    expire = datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM) # token create 
    return token

# Login API(token generate)
@app.post("/login")
def login(username:str,password:str):
    if username!="admin" or password!= "1234":
        raise HTTPException(
            status_code=401,
            detail="Invalid Username and password"
        )
    token = create_token({
        "sub":username
    })
    return{
        "access_token":token
    }
    
# token verificaton

def verify_token(token:str =Header(None)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM]) # upor a jataq encode korchilam akahne decode korlam
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invaliid or expired token"
        )

# protected route (verifyed user rai akhane aste parbe )
@app.get("/secure")
def secure_data(user=Depends(verify_token)):
    return{
        "message":"Secure Data Accessed",
        "user":user
    }