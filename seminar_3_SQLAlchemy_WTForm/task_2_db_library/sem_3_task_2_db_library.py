# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template
import random
from task_2_db_library.sem_3_task_2_models import db, Book, Author, BookAuthor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_2_db_library.db'
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('add-datas')
def add_datas():
    for i in range (1,11):
        new_author = Author(first_name = f'Author_name_{i}',
                          last_name = f'Author_lastname_{i}',)
        db.session.add(new_author)
    for i in range (1,21):
        new_book = Book(name = f'Book-{i}',
                        year=random.randint(1825, 2017),
                        count=random.randint(1, 7)
                        )
        db.session.add(new_book)
    for i in range(1, 15):
        book_author = BookAuthor(book_id=random.randint(1,20),
                                 author_id = random.randint(1,10))
        db.session.add(book_author)
    db.session.commit()
    print('Datas added')

@app.route('/book/')
def books():
    books = Book.query.all()
    context = {'books':books}
    return render_template('books.html', **context)

if __name__ == '__main__':
    app.run(debug=True)