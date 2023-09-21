from fastapi import APIRouter
from typing import List
from db import users, database
from models.user import User, UserIn


router = APIRouter()

# Заполнение тестовыми пользователями
@router.get('/fake_users/{count}')
async def create_fake_users(count:int):
    for i in range (1, count+1):
        query = users.insert().values(
            username=f'Username_{i}',
            email=f'mail{i}@m.mj',
            password=f'pwd{i}')
        await database.execute(query)
    return {'message': f'{count} fake users created'}

# Показать всех пользователей
@router.get('/users/', response_model=List[User])
async def show_all_users():
    query = users.select()
    return await database.fetch_all(query)


# Показать одного конкретного пользователя
@router.get('/user/{id}', response_model=User)
async def show_one_user(id:int):
    query = users.select().where(users.c.id == id)
    return await database.fetch_one(query)


# Создать нового пользователя
@router.post("/users/")
async def create_user(user: UserIn):
    query = users.insert().values(username=user.username, email=user.email,password=user.password)
    await database.execute(query)
    return {'Successfully added: ': user}


# Редактировать данные пользователя
@router.put('/user_update/{id}')
async def update_user(id:int, new_datas: UserIn):
    query = users.update().where(users.c.id == id).values(username=new_datas.username,
                                                          email=new_datas.email,
                                                          password=new_datas.password)
    await database.execute(query)

    return {'Successfully updated: ': f'user with id {id} {new_datas}'}


# Удалить пользователя
@router.delete('/del_user/{id}')
async def delete_user(id:int):
    query = users.delete().where(users.c.id == id)
    await database.execute(query)
    return {'message': 'User deleted'}