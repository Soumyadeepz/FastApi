
# by using fastapi
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news(page: int=1,limit:int=5): # start korchi 1 thake ar akta page 5 ta data highestv show korabo
    url = "https://news.ycombinator.com/" # ai website ar data extract korbo
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text,"html.parser") # response text format a chai so response.text
    title=[]
    for item in soup.find_all("span",class_="titleline"):#(tag,classname)
        title.append(item.text)
        
    #Pagination Logic
    start =(page-1)*limit
    end = start+limit
    
    return{
        "page":page, # konsa page
        "limit":limit,# kota item dekhabo per page
        "total":len(title),# total item kota ache
        "data":title[start:end] # data display korbe start theke end porjonto 
    }