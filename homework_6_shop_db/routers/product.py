from random import randint

from fastapi import APIRouter
from typing import List
from db import products, database
from models.product import Product, ProductIn


router = APIRouter()

# Заполнение тестовыми товарами
@router.get('/fake_prods/{count}')
async def create_fake_prods(count:int):
    for i in range (1, count+1):
        query = products.insert().values(
            productname=f'Prod_{i}',
            description=f'Description for product {i}',
            price = float(randint(0,150)))
        await database.execute(query)
    return {'message': f'{count} fake products created'}

# Показать все товары
@router.get('/prods/', response_model=List[Product])
async def show_all_prods():
    query = products.select()
    return await database.fetch_all(query)


# Показать один конкретный товар
@router.get('/prod/{id}', response_model=Product)
async def show_one_prod(id:int):
    query = products.select().where(products.c.id == id)
    return await database.fetch_one(query)


# Создать новый товар
@router.post("/prods/")
async def create_prod(prod: ProductIn):
    query = products.insert().values(productname=prod.productname,
                                     description=prod.description,
                                     price=prod.price)
    await database.execute(query)
    return {'Successfully added: ': prod}


# Редактировать данные товара
@router.put('/prod_update/{id}')
async def update_user(id:int, new_datas: ProductIn):
    query = products.update().where(products.c.id == id).values(productname=new_datas.productname,
                                                                description=new_datas.description,
                                                                price=new_datas.price)
    await database.execute(query)

    return {'Successfully updated: ': f'user with id {id} {new_datas}'}


# Удалить товар
@router.delete('/del_prod/{id}')
async def delete_prod(id:int):
    query = products.delete().where(products.c.id == id)
    await database.execute(query)
    return {'message': 'User deleted'}