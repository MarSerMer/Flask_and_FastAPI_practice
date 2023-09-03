from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/base/')
def base():
    return render_template('base.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/coats/')
def coats():
    coats = [{'color': 'Красная', 'price': 15, 'size': 44},
             {'color': 'Зеленая', 'price': 18, 'size': 42},
             {'color': 'Синяя', 'price': 19, 'size': 40},
             {'color': 'Белая', 'price': 11, 'size': 42},
             {'color': 'Оранжевая', 'price': 20, 'size': 46}, ]
    return render_template('coats.html', coats=coats)


@app.route('/shoes/')
def shoes():
    shoes = [{'type': 'Кроссовки', 'price': 12, 'size': 39},
             {'type': 'Сапоги', 'price': 22, 'size': 39},
             {'type': 'Ботинки', 'price': 17, 'size': 39}, ]
    return render_template('shoes.html', shoes=shoes)


if __name__ == '__main__':
    app.run(debug=True)
