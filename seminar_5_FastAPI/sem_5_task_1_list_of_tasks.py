# Задание №1
# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str


class TaskIn(BaseModel):
    title: str
    description: Optional[str]
    status: str


tasks: list[Task] = []


@app.get('/')
async def root():
    return {"message": "Hello World!"}


@app.get('/tasks/', response_model=list[Task])
async def get_tasks():
    return tasks


@app.post('/tasks/', response_model=list[TaskIn])
async def add_tasks(new_task: TaskIn):
    tasks.append(Task(id=len(tasks) + 1,
                      title=new_task.title,
                      description=new_task.description,
                      status=new_task.status))
    return tasks


@app.put('/tasks/',response_model=Task)
async def edit_task(id: int, new_task: TaskIn):
    if id > len(tasks):
        raise HTTPException(status_code=404,detail='Task not found')
    for i in range(0,len(tasks)):
        if tasks[i].id == id:
            current_task = tasks[id-1]
            current_task.title = new_task.title
            current_task.description = new_task.description
            current_task.status = new_task.status
            return current_task
    raise HTTPException(status_code=404,detail='Task not found')



@app.delete('/tasks/',response_model=dict)
async def delete_task(id: int):
    if id > len(tasks):
        raise HTTPException(status_code=404,detail='Task not found')
    for i in range(0,len(tasks)):
        if tasks[i].id == id:
            tasks.remove(tasks[i])
            return {'Message': 'Task was deleted'}
    raise HTTPException(status_code=404,detail='Task not found')


if __name__ == '__main__':
    uvicorn.run(
        "sem_5_task_1_list_of_tasks:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
