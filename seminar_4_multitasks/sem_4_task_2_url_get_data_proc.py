# Задание №2
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте процессы.

import requests
from multiprocessing import Process
import time

urls = ['https://gb.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://dzen.ru/',
        'https://www.gto.ru/files/uploads/stages/5cdd1ebfacd54.pdf',
        'https://spb.galileopark.ru/contacts/']

def get_datas_from_sites(url):
    response = requests.get(url)
    filename = 'sem_4_task_2_files/multiprocessing_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f}seconds")

processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=get_datas_from_sites, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
