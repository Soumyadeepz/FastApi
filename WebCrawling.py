
# by using normal python
# import requests
# from bs4 import BeautifulSoup

# url="http://example.com"

# response = requests.get(url)
# soup= BeautifulSoup(requests.text,"html.parser")# BeautifulSoup -> html parse korar janna use hoy

# print(soup.title.text) # website ar ja title thakbe print hoye jabe 

# by using fastapi
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news():
    url = "https://indianexpress.com" # ai website ar data extract korbo
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text,"html.parser") # response text format a chai so response.text
    title=[]
    for item in soup.find_all("a",class_="topblockNews_sidebarLink"):#(tag,classname)
        title.append(item.text)
        
        return{
            "news":title[:5]
        }