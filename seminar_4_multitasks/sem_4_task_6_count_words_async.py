# Задание №6
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход.

import asyncio
import os
import time

PATH = 'sem_4_task_1_files'
words_count = 0

async def count_words(file_name):
    global words_count
    with open(file_name, 'r', encoding='utf-8') as f:
        count = len(f.read().split())
    words_count += count
    print(f'File: {file_name} has {count} words inside.')

async def main():
    tasks = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            filename = os.path.join(root, filename)
            task = asyncio.create_task(count_words(filename))
            tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
    print(f'Finally we have: {words_count} words')