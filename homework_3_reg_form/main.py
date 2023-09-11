# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
from models import db, User
from forms import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
db.init_app(app)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')



@app.route('/', methods=['GET', 'POST'])
def user_reg():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        password_special = generate_password_hash(form.password.data)
        user = User(firstname=firstname,
                    lastname=lastname,
                    email=email,
                    password=password_special)
        db.session.add(user)
        db.session.commit()
        return f'New user registered: {firstname} {lastname} {email} {password} {password_special}'
    return render_template('user_reg.html', form=form)

@app.route('/show_users/')
def show_users():
    users = User.query.all()
    return f'{list(users)}'

if __name__ == '__main__':
    app.run(debug=True)