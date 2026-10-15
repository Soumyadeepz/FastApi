# sqlAlchemy
from fastapi import FastAPI,Depends
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session


app = FastAPI()

DATABASE_URL = "sqlite:///./test1.db"

# database connect 
engine = create_engine(
    DATABASE_URL,
    connect_args ={"check_same_thread":False}
)

# session db te operation handle korbo
sessionLocal = sessionmaker(bind=engine) # sessiondb ke engine ar sathe bind kore dibo

# model bananor janna base
Base = declarative_base()

# model create
class Todo(Base):
    __tablename__ ="todos"
    
    id =Column(Integer,primary_key=True,index=True)
    title=Column(String)
    completed= Column(String)

#table create korbo database a 
Base.metadata.create_all(bind=engine) # atar through i table create hobe test1.db te

# common api - check that each api session get db or not
# protita api ke db access korte diba
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def home(db:Session=Depends(get_db)):
    return{
        "message":"DB connected fine"
    }