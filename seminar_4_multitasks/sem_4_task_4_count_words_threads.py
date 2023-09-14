# Задание №4
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.

import threading
import os

PATH = 'sem_4_task_1_files'
words_count = 0

def count_words(file_name):
    global words_count
    with open(file_name, 'r', encoding='utf-8') as f:
        count = len(f.read().split())
    words_count += count
    print(f'File: {file_name} has {count} words inside.')


if __name__ == '__main__':
    threads = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            filename = os.path.join(root,filename)
            thread = threading.Thread(target=count_words, args=[filename])
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()

    print(f'Finally we have: {words_count} words')

