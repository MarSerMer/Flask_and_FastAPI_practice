# Задание №2
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.
from enum import Enum

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi import HTTPException

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str]
    genre: str


class MovieIn(BaseModel):
    title: str
    description: Optional[str]
    genre: str


movies: list[Movie] = []
for i in range(1, 6):
    movie = Movie(id=i,
                  title=f'Movie_{i}',
                  description=f'Descr_{i}',
                  genre='G')
    movies.append(movie)
for i in range(6, 11):
    movie = Movie(id=i,
                  title=f'Movie_{i}',
                  description=f'Descr_{i}',
                  genre='T')
    movies.append(movie)


@app.get('/movies/{genre}', response_model=list[Movie])
async def get_list_of_movies(genre: str):
    res: list[Movie] = []
    for i in range(0, len(movies)):
        if movies[i].genre == genre:
            res.append(movies[i])
    return res


@app.post('/movies/', response_model=Movie)
async def add_movies(new_movie: MovieIn):
    movie_to_add = Movie(id=len(movies) + 1,
                         title=new_movie.title,
                         description=new_movie.description,
                         genre=new_movie.genre)
    movies.append(movie_to_add)
    return movie_to_add


@app.get('/all/', response_model=list[Movie])
async def show_all_movies():
    return movies


if __name__ == '__main__':
    print(movies)

    uvicorn.run(
        "sem_5_task_2_films:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
