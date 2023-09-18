# Задание №3
# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.

# Задание №4
# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте маршрут для обновления информации о пользователе (метод PUT).

# Задание №5
# Создать API для удаления информации о пользователе из базы данных.
# Приложение должно иметь возможность принимать DELETE запросы и
# удалять информацию о пользователе из базы данных.
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте проверку наличия пользователя в списке и удаление его из списка.

# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение должно использовать
# шаблонизатор Jinja для динамического формирования HTML страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password. Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, constr

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=6, max_length=16)


class User(UserIn):
    id: int

    def __str__(self):
        return f'User {self.id}: {self.name} - {self.email}.'


users: list[User] = []
all_id: list[int] = []
for i in range(1, 11):
    new_user = User(id=i, name=f'Name-{i}', email=f'mail{i}@users.users', password='secret')
    print(new_user)
    users.append(new_user)
    all_id.append(new_user.id)


@app.get('/all_users/', response_class=HTMLResponse)
async def show_all_users(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.post('/add_user/', response_model=User)
async def add_user(new: UserIn):
    id = len(users) + 1
    while True:
        if id in all_id:
            id += 1
        else:
            break
    new_user = User(id=id, name=new.name, email=new.email, password=new.password)
    users.append(new_user)
    all_id.append(new_user.id)
    return new_user

@app.post('/add_user_form/',response_class=HTMLResponse)
async def add_user_form(request:Request):
    datas = await request.form()
    id = len(users) + 1
    while True:
        if id in all_id:
            id += 1
        else:
            break
    new_user = User(id=id,
                    name=datas.get('name'),
                    email=datas.get('email'),
                    password=datas.get('password'))
    users.append(new_user)
    all_id.append(new_user.id)
    return '<p>User added</p>'

@app.put('/change_datas/', response_model=dict)
async def change_datas(id: int, new_datas: UserIn):
    if id in all_id:
        for user in users:
            if user.id == id:
                user.name = new_datas.name
                user.email = new_datas.email
                user.password = new_datas.password
                return {'message': 'datas updated', "new info": user}
        raise HTTPException(status_code=404, detail='User not found')
    raise HTTPException(status_code=404, detail='ID not found')


@app.get('/delete_user/{id}', response_model=dict)
async def delete_user(id: int):
    if id in all_id:
        for user in users:
            if user.id == id:
                users.remove(user)
                return {'Message': f'User {id} was deleted'}
    raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
