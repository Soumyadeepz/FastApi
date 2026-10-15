
# import requests

# id ar basis a data chaile just posts ar por /1 dila id =1 ar data paye jabo
# response = requests.get("https://jsonplaceholder.typicode.com/posts")#api url paste korbo

# data = response.json()
# print(data) #print(data[:2]) # duta data chaile avabe likha hoy 

from fastapi import FastAPI,HTTPException
import requests # http request send korar janna use korchi ai library ta 
#.json() likhchi response ke python object a bananor janna
# readymaid service nijer according dibo bole third party api use korchi

app = FastAPI()

#get all data
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

# single data chaile
@app.get("/posts/{post_id}")
def get_post(post_id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=404,detail="Page not found")
    
    return response.json()