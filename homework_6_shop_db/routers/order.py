import datetime
import random
from fastapi import APIRouter
from typing import List
from sqlalchemy import select
from models.order import OrderIn, Order
from db import database, orders, users, products

router = APIRouter()


# Заполнение тестовыми заказами
@router.get('/fake_orders/{count}')
async def create_fake_orders(count: int):
    for i in range(count):
        clients = users.select()
        list_of_clients = await database.fetch_all(clients)
        prods = products.select()
        list_of_prods = await database.fetch_all(prods)
        query = orders.insert().values(user_id=random.choice([user_id[0] for user_id in list_of_clients]),
                                       product_id=random.choice([product_id[0] for product_id in list_of_prods]),
                                       orderdate=datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
                                       status=random.choice(['done', 'on its way', 'needs support']))
        await database.execute(query)
    return {'message': f'{count} fake orders created'}


# Показать все заказы
@router.get('/orders/', response_model=List[Order])
async def show_all_orders():
    query = orders.select()
    return await database.fetch_all(query)


# Показать все заказы очень подробно
@router.get('/orders_detailed/')
async def show_all_orders_b():
    query = select(orders.c.id, orders.c.orderdate, orders.c.status,
                   products.c.id.label('product_id'), products.c.productname, products.c.description, products.c.price,
                   users.c.id.label('user_id'), users.c.username, users.c.email, users.c.password). \
        join(products).join(users)
    return await database.fetch_all(query)


# Показать один конкретный заказ
@router.get('/orders/{id}', response_model=Order)
async def show_one_order(id: int):
    query = orders.select().where(orders.c.id == id)
    return await database.fetch_one(query)


# Создать новый заказ
@router.post("/orders/")
async def create_prod(new_datas: OrderIn):
    query = orders.insert().values(user_id=new_datas.user_id,
                                   product_id=new_datas.product_id,
                                   orderdate=new_datas.orderdate,
                                   status=new_datas.status)
    await database.execute(query)
    return {'Successfully added: ': new_datas}


# Редактировать данные заказа
@router.put('/order_update/{id}')
async def update_user(id: int, new_datas: OrderIn):
    query = orders.update().where(orders.c.id == id).values(user_id=new_datas.user_id,
                                                            product_id=new_datas.product_id,
                                                            orderdate=new_datas.orderdate,
                                                            status=new_datas.status)
    await database.execute(query)
    return {'Successfully updated: ': f'user with id {id} {new_datas}'}


# Удалить заказ
@router.delete('/del_order/{id}')
async def delete_order(id: int):
    query = orders.delete().where(orders.c.id == id)
    await database.execute(query)
    return {'message': 'User deleted'}
