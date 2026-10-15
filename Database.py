
# sqlLite
import sqlite3
from fastapi import FastAPI
app =FastAPI()
# connect hole db open hobe
conn = sqlite3.connect("test.db",check_same_thread=False) # duta parameter dita hoy  1st parameter a file name dibo jekhane databasen store korte chachhi , 2nd parameter check korbe sam,e thread use korchi kina 

# cursor a sql run hobe
cursor =conn.cursor()# cursor sql query ke connect korte kaje lage

# table create 
# query run korabe execute
cursor.execute('''
CREATE TABLE IF NOT EXISTS todos(
        id INTEGER PRIMERY KEY,
        title TEXT,
        completed TEXT
    )
''')
# change ke save korabo
# query db te save hobe 
conn.commit()

@app.get("/")
def home():
    return{
        "message":"sqllite connected"
    }