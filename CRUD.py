
from fastapi import FastAPI
from pydantic import BaseModel
app= FastAPI()

todos= [] # here we store lists

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"Todo added",
        "data":todo
    }
@app.get("/todos")
def get_todos():
    return todos

# to get single data we need path params
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in  todos:
        if todo.id == todo_id:
            return todo
    return {"error":"todo not found"}

@app.put("/todos/{todo_id}") # id ar basis a update korbo so todo_id
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return{
                "message":"Data updated",
                "data":updated_todo
            }
    return {"error":"todo not found"}

@app.delete("/todos/{todo_id}")
def delete_id(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {
                "message":"Data deleted",
            }
    return {"error":"Todo not found"}