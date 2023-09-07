# Задание №1
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

from flask import Flask, render_template, redirect, url_for, request, flash,abort
from pathlib import PurePath, Path
from werkzeug.utils import secure_filename
import logging


app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
logger = logging.getLogger(__name__)

@app.route('/')
def base():
    return render_template('base.html')


@app.route('/next')
def next_page():
    return 'Hello, Username!'


# Задание №2
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

@app.route('/picture/', methods=['GET', 'POST'])
def picture_form():
    context = {'task': 'Форма для загрузки файла'}
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'File {file_name} is uploaded on the server.'
    return render_template('page_2.html', **context)


# Задание №3
# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия
# логина и пароля и переход на страницу приветствия пользователя или страницу с ошибкой.
@app.route('/welcome/')
def welcome_user():
    return render_template('page_3_welcome.html')


@app.route('/wrong_login_or_password/')
def wrong_login_or_password():
    return render_template(('page_3_wrong_login_or_password.html'))


@app.route('/log_in/', methods=['GET', 'POST'])
def log_in():
    context = {'task': 'Логин-пароль'}
    pairs = [{'login': 'aaa', 'password': 'aaa'},
             {'login': '321', 'password': '321'},
             {'login': '1718', 'password': '1718'}, ]
    if request.method == 'POST':
        login = str(request.form.get('login'))
        password = str(request.form.get('password'))
        print(f'{login} {password}')
        correct: bool = False
        for pair in pairs:
            print(pair)
            if login in pair.values():
                if pair['login'] == login and pair['password'] == password:
                    correct = True
                    break
        if correct:
            return redirect(url_for('welcome_user'))
        else:
            return redirect(url_for('wrong_login_or_password'))
    return render_template('page_3.html', **context)


# # Задание №4
# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте
# и переход на страницу с результатом.
@app.route('/count_words/', methods=['GET', 'POST'])
def count_words():
    context = {'task': 'Подсчет слов'}
    if request.method == 'POST':
        text = str(request.form.get('text'))
        count = len(text.split())
        return f'Количество слов вашем тексте: {count}.'
    return render_template('page_4.html', **context)


# Задание №5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    context = {'task': 'Калькулятор'}
    signs = ['+', '-', '/', '*']
    if request.method == 'POST':
        try:
            num_1 = float(request.form.get('num_1'))
            num_2 = float(request.form.get('num_2'))
        except ValueError:
            return f'Что-то какие-то цифры странные, не знаю я таких...'
        sign = str(request.form.get('sign'))
        res = None
        if sign not in signs:
            return f'Что-то знак вообще странный какой-то, такого я не знаю...попробуйте посчитать на листочке!'
        else:
            if sign == '+':
                res = num_1 + num_2
            elif sign == '-':
                res = num_1 - num_2
            elif sign == '*':
                res = num_1 * num_2
            else:
                try:
                    res = round(num_1 / num_2, 3)
                except ZeroDivisionError:
                    res = 'На ноль делить, конечно, интересно...бесконечность будет!'
        return f'{res}.'
    return render_template('page_5.html', **context)


# Вот так сделали на семинаре (template 'calculator'), хорошее решение со знаками!
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        number_1 = request.form.get('number_1')
        number_2 = request.form.get('number_2')
        operation = request.form.get('operation')
        match operation:
            case 'add':
                return f'{int(number_1) + int(number_2)}'
            case 'subtract':
                return f'{int(number_1) - int(number_2)}'
            case 'multiply':
                return f'{int(number_1) * int(number_2)}'
            case 'divide':
                if number_2 == '0':
                    return f'Нельзя делить на ноль'
                return f'{int(number_1) / int(number_2)}'
    context = {
        'task': 'Задание_5'
    }
    return render_template('calculator.html', **context)


# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и
# переход на страницу с результатом или на страницу с ошибкой
# в случае некорректного возраста.

@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    context = {'task': 'Проверка допуска по возрасту'}
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if int(age) >= 18:
            return f'Welcome {name}!'
        else:
            abort(403)
    return render_template('page_6_check_age.html', **context)


@app.errorhandler(403)
def page_not_found(e):
    logger.warning(e)
    context = {'task': 'Эта страница не для вас, увы'}
    return render_template('page_6_error_403.html', **context), 403


# Задание №7
# Создать страницу, на которой будет форма для ввода числа и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.
@app.route('/show_res/<float:number>')
def show_res(number):
    return f'Квадрат числа {number}: {number ** 2}'


@app.route('/count_square/', methods=['GET', 'POST'])
def count_square():
    context = {'task': 'Вычисление квадрата'}
    if request.method == 'POST':
        number = float(request.form.get('number'))
        return redirect(url_for('show_res', number=number))
    return render_template('page_7_square.html', **context)

# Задание №8
# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

@app.route('/flash_hello/', methods=['GET', 'POST'])
def flash_hello():
    context = {'task': 'Вывод флеш-сообщения'}
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('flash_hello'))
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('flash_hello'))
    return render_template('page_8_ask_name.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
