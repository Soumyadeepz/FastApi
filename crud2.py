# sqlAlchemy
from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session


app = FastAPI()

# Database URL
DATABASE_URL = "sqlite:///./test1.db"

# Engine create (DB connection)
engine = create_engine(
    DATABASE_URL,
    connect_args ={"check_same_thread":False}
)

# Session (DB operations ke liye)
sessionLocal = sessionmaker(bind=engine) # sessiondb ke engine ar sathe bind kore dibo

# Base (model ke liye)
Base = declarative_base()

# table (model)
class Todo(Base):
    __tablename__ ="todos"
    
    id =Column(Integer,primary_key=True,index=True)
    title=Column(String)
    completed= Column(String)

# Table create
Base.metadata.create_all(bind=engine) # atar through i table create hobe test1.db te

# Dependency (DB session provide karega)
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# create api

@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
    todo = Todo(title=title,completed="False")# object create , initially kichu na pale title ar moddha title chole jabe ar false thakbe 
    db.add(todo)# db te add korchi
    db.commit()# db te save korchi
    db.refresh(todo)# db refresh korchi jata id paye jai db te latest data ar
    return{
        "message":"Todo created",
        "data":todo
    }
    
# read all data
@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    todos = db.query(Todo).all()
    return{
        "Total":len(todos),
        "data":todos
    }
    
# read data by id one by ine
@app.get("/todos/{todo_id}")
def get_todo(todo_id=int,db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if not todo: # jadi id todo ar moddhe na thake 
        raise HTTPException(status_code=404,detail="Todo not found")
    return todo

# update data 
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
        
    if not todo: # jadi id todo ar moddhe na thake 
        raise HTTPException(status_code=404,detail="Todo not found")
    # title update korbo
    todo.title = title
    db.commit()# update korchi tai save o korte hobe 
    db.refresh(todo)
    return{
        "message":"Todo updated",
        "data":todo
    }
    
# Delete api
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id==todo_id).first()
    
    if not todo:
        raise HTTPException(status_code =404,detail="Todo not found")
    db.delete(todo)
    db.commit()
    
    return{
        "message":"Todo deleted"
    }