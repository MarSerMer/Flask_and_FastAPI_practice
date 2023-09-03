# Задание №1
# Напишите простое веб-приложение на Flask, которое будет
# выводить на экран текст "Hello, World!".
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Задание №2
# Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше вебприложение:
# ○ страницу "about"
# ○ страницу "contact".
@app.route('/about/')
def about():
    return 'This is content for "About" page'


@app.route('/contact/')
def contact():
    return 'This is content for "Contact" page'


# Задание №3
# Написать функцию, которая будет принимать на вход два
# числа и выводить на экран их сумму.
@app.route('/<int:a>/<int:b>/')
def sum_(a: int, b: int) -> str:
    return f'{a + b}'


# Задание №4
# Написать функцию, которая будет принимать на вход строку и
# выводить на экран ее длину.
@app.route('/textlength/<text>/')
def show_text_length(text: str) -> str:
    return f'There are {len(text)} symbols in this text.'


# Задание №5
# Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".
# html = """<h>Моя первая HTML страница</h> <p>Привет, мир!</p>
# """
# @app.route('/html/')
# def show_html():
#     return html
@app.route('/html/')
def show_html():
    return render_template('task_5.html')


# Задание №6
# Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через
# контекст.

@app.route('/students/')
def students():
    students = [{'First_name': 'Jack',
                 'Last_name': 'Sparrow',
                 'Age': 15,
                 'Average_score': 3.7},
                {'First_name': 'Kofa',
                 'Last_name': 'Ioh',
                 'Age': 112,
                 'Average_score': 5.0},
                {'First_name': 'Aang',
                 'Last_name': 'Avatar',
                 'Age': 11,
                 'Average_score': 4.5}]
    context = {'title': 'Students',
               'students': students}
    return render_template('task_6.html', **context)


@app.route('/students/table/')
def students_table_view():
    head = {'First_name': 'Имя',
            'Last_name': 'Фамилия',
            'Age': 'Возраст',
            'Average_score': 'Средний балл'}
    students = [{'First_name': 'Jack',
                 'Last_name': 'Sparrow',
                 'Age': 15,
                 'Average_score': 3.7},
                {'First_name': 'Kofa',
                 'Last_name': 'Ioh',
                 'Age': 112,
                 'Average_score': 5.0},
                {'First_name': 'Aang',
                 'Last_name': 'Avatar',
                 'Age': 11,
                 'Average_score': 4.5}]
    return render_template('task_6-2.html', **head, students=students)


# Задание №7
# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.

@app.route('/news/')
def news():
    news_block = [{'title': 'News 1',
                   'description': 'News 1 shortly',
                   'created': datetime.now().strftime('%H:%M - %m.%d.%Y года')},
                  {'title': 'News 2',
                   'description': 'News 2 shortly',
                   'created': datetime.now().strftime('%H:%M - %m.%d.%Y года')},
                  {'title': 'News 3',
                   'description': 'News 3 shortly',
                   'created': datetime.now().strftime('%H:%M - %m.%d.%Y года')}]
    return render_template('task_7.html',news_block=news_block)

if __name__ == '__main__':
    app.run()
