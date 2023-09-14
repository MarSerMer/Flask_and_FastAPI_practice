# Задание
# Написать программу, которая скачивает изображения с заданных URL-адресов
# и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле,
# название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого
# изображения и общем времени выполнения программы.

import time
from multiprocessing import Process
from sys import argv

import requests

urls = ['https://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg',
        'https://iphoneroot.com/wp-content/uploads/2011/07/Mac-OS-X-Lion-Galaxy-500x312.jpg',
        'https://a.d-cd.net/d9e8d6es-1920.jpg',
        'https://storage.vsemayki.ru/images/0/3/3467/3467647/previews/people_7_manshort_front_white_700.jpg',
        'https://ir.ozone.ru/s3/multimedia-7/wc1000/6443464243.jpg']
URL = 'https://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg'
FOLDER_NAME = 'images_multiproc'


def download_image(url: str = URL, foldername: str = FOLDER_NAME) -> None:
    start_time = time.time()
    response = requests.get(url)
    filename = url.split('/')[-1]
    with open(f'{foldername}/{filename}', 'wb') as f:
        f.write(response.content)
    print(f'Picture {filename} was downloaded. It took {time.time() - start_time:.2f} seconds.')


def main(urls: list) -> None:
    processes = []
    for url in urls:
        if url.endswith('.jpg') or url.endswith('.jpeg'):
            process = Process(target=download_image, args=(url,))
            processes.append(process)
            process.start()
    for process in processes:
        process.join()

if __name__ == '__main__':
    urls_from_terminal = argv[1:]
    # main(urls)
    main(urls_from_terminal)
