
# pip install slowapi

from fastapi import FastAPI,Request
from slowapi import Limiter

from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse


app = FastAPI()

# limiter set up
limiter = Limiter(key_func= get_remote_address) # get_remote_address protita user ar specific address ke track korbe 

app.state.limiter = limiter

#error handle
@app.exception_handler(RateLimitExceeded)
def rate_limit_hander(request: Request,exc:RateLimitExceeded):
    return JSONResponse(
        status_code = 429,
        content={
            "detail":"Too many Requests"
        }
    )
# rate limiter api
@app.get("/data")
@limiter.limit("5/minute") # 5 request per minute 
def get_data(request:Request):
    return{
        "message":"Success"
    }