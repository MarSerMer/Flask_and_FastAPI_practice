# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class UserIn(BaseModel):
    name: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str

    def __repr__(self):
        return f'{self.id} : {self.name} - {self.email}'


class User(UserIn):
    id: int


users: list[UserOut] = []
for i in range(1, 11):
    new_user_out = UserOut(id=i, name=f'Name-{i}', email=f'mail{i}@users.users')
    print(new_user_out)
    users.append(new_user_out)
print('WHOLE LIST:', users)


@app.get('/show_users/', response_class=HTMLResponse)
async def show_users(request: Request):
    return templates.TemplateResponse('task_6_users.html', {'request': request, 'users': users})


if __name__ == '__main__':
    print(users)

    uvicorn.run(
        "sem_5_task_6_users_Jinja:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
