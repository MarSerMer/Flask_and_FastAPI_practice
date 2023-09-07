# Задание
# Создать страницу, на которой будет форма
# для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия,
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую
# будет удалён cookie-файл с данными пользователя
# и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)

@app.route('/welcome/')
def welcome():
    name = request.cookies.get('username')
    if name:
        return render_template('welcome.html', name=name)
    return redirect('/')



@app.route('/base/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def base():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('username',name)
        response.set_cookie('usermail',email)
        return response
    return render_template('base.html')

@app.route('/out')
def del_cookies():
    response = make_response(redirect('/'))
    response.delete_cookie('username')
    response.delete_cookie('usermail')
    return response

if __name__ == '__main__':
    app.run(debug=True)