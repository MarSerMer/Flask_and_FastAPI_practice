# Задание №5
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.

import multiprocessing
import os

PATH = 'sem_4_task_1_files'
words_count = multiprocessing.Value('i', 0)

def count_words(file_name,words_count):
    with open(file_name, 'r', encoding='utf-8') as f:
        count = len(f.read().split())
    with words_count.get_lock():
        words_count.value += count
    print(f'File: {file_name} has {count} words inside.')


if __name__ == '__main__':
    processes = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            filename = os.path.join(root, filename)
            p = multiprocessing.Process(target=count_words,args=(filename,words_count))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()

    print(f'Finally we have: {words_count.value:_} words')
