from fastapi import FastAPI,HTTPException,Depends
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime,timedelta,timezone

app = FastAPI()

#JWT Config
SECRET_KEY="mysecret"
ALGORITHM = "HS256" # algorithm to hash token
ACCESS_TOKEN_EXPIRE_MINUTES=30

# password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

#Oauthsetup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Dummy user DB
fake_user_db ={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}

#hash Pssword
def hash_password(password:str):
    return pwd_context.hash(password)
# verify password
def verify_password(plain_password,hased_password):
    return pwd_context.verify(plain_password,hased_password)


# create token
def create_token(data: dict):# token dict ar form a thakbe 
    to_encode = data.copy() # data copy kore rakhbo
    expire = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp":expire
    })
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM) # token create 
    return token

# Login API(Oauth2 from)
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )
    access_token = create_token({"sub":form_data.username})
    return{
        "access_token":access_token,
        "token_type":"bearer"
    }
# token verificaton

def verify_token(token:str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        return username
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
        
#Protected Route
@app.get("/protected")
def protected_route(username: str = Depends(verify_token)):
    return{
        "message":"Hello you have access to this protected route",
        "user":username
    }