# Задание №1
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
# возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название
# факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их факультета.
import random
from flask import Flask, render_template
from seminar_3_SQLAlchemy_WTForm.task_1_db_students.sem_3_task_1_models import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_1_db.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('add-datas')
def add_students():
    for i in range (1,4):
        new_faculty = Faculty(name = f'Faculty_{i}',)
        db.session.add(new_faculty)
    for i in range (1,11):
        new_student = Student(first_name = f'Student{i}',
                              last_name = f'Lastname{i}',
                              age = 15 + i,
                              gender = random.choice(('male','female')),
                              group = random.randint(1,7),
                              id_faculty = random.randint(1,3)
                              )
        db.session.add(new_student)
    db.session.commit()
    print('Datas added')

@app.route('/')
def show_students():
    students = Student.query.all()
    context = {'students':students}
    return render_template('students.html', **context)

if __name__ == '__main__':
    app.run(debug=True)