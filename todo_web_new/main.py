from typing import Optional
from fastapi import FastAPI
from database import TodoList


app = FastAPI()
todoList = TodoList()
todoList.initialize()
todoList.connect()
todoList.open()


@app.get("/")
def read_todos():
    sql = "SELECT * FROM `todo`;"
    return todoList.select(sql)


@app.get("/create/{item_name}")
def create_todo(item_name):
    sql = "INSERT INTO todo (TODO_NAMES) VALUES ('"+item_name+"');"
    return todoList.select(sql)


@app.get("/delete/{item_id}")
def delete_todo(item_id):
    sql = "DELETE FROM todo WHERE TODO_ID = "+item_id+";"
    return todoList.select(sql)


# @app.get("/isPri/{item_id}")
# def delete_todo(item_id):
#     if todoList.select("SELECT todo WHERE IS_PRIORITY = 0")
#     sql = "UPDATE todo SET IS_PRIORITY = 1 WHERE TODO_ID = "+item_id+";"
#     return todoList.select(sql)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


# @app.get("/")
# def delete_todo("/items/"):
#     sql = "SELECT * FROM `todo`;"
#     return todoList.select(sql)




