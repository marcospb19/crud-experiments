from typing import Dict, Optional, List, TypeVar
from fastapi import FastAPI, status, HTTPException
from todo import Todo, TodoKey, TodoValue
from id_generator import IdGenerator, Id
from json_types import JsonObject, JsonList

# Used to generate unique Ids for our `todos` dict keys
id_gen = IdGenerator()
todos: Dict[Id, Todo] = {}

app = FastAPI()

@app.get('/todos')
def index() -> JsonList[Todo]:
    return list(todos.values())

@app.get('/todos/{item_id}')
def show(item_id: Id) -> JsonObject[Optional[Todo]]:
    return { 'item': todos.get(item_id, None) }

@app.post('/todos', status_code=status.HTTP_201_CREATED)
def create(entry: dict) -> JsonObject[int]:
    if 'description' not in entry or 'category' not in entry:
        raise HTTPException(status_code=400, detail='JSON missing "description" or "category" field')

    new_id: Id = id_gen.next()
    todos[new_id] = Todo(entry['description'], entry['category'], new_id)
    return { 'id': new_id }

@app.delete('/todos/{item_id}')
def delete(item_id: int) -> JsonObject[bool]:
    delete_result: bool = todos.pop(item_id, None) is not None
    return { "operation_succeeded": delete_result }

@app.put('/todos', status_code=status.HTTP_202_ACCEPTED)
def update(entry: dict):
    if 'id' not in entry or 'todo' not in entry:
        raise HTTPException(status_code=400, detail='JSON missing "id" or "todo" field')

    if entry['id'] not in todos:
        raise HTTPException(status_code=404, detail=f'Todo resource by id {entry["id"]} not found')

    del entry['id']
