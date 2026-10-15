
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import os
# from dotenv import load_dotenv
from config import settings
app = FastAPI()
# load_dotenv()
# Allowed Origins(Front-end URL)
# origins =[
#     "http://localhost:5173"
# ]


origins=settings.origins
#origins = os.getenv("ORIGINS")
# SECRET_KEY = os.getenv("SECRET_KEY")
# DB_URL = os.getenv("DB_URL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials= True,
    allow_headers=["*"],
    allow_methods=["*"] # all methods get,put,post ,delete sob allow
)

@app.get("/")
def home():
    return{
        "message":"cors enable api"
    }