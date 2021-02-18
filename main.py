from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    return """
    Человечество вырастает из детства.
    <br>
    Человечеству мала одна планета.
    <br>
    Мы сделаем обитаемыми безжизненные пока планеты.
    <br>
    И начнем с Марса!
    <br>
    Присоединяйся!
    """


@app.route('/image_mars')
def image():
    return f"""
    <!doctype html>
    <html>
        <head>
        <title>Привет, Марс!</title>
        </head>
        <body>
        <h1>Жди нас, Марс!</h1>
        <img src='{url_for('static', filename='img/mars.jpg')}' alt='Image not found'>
        <br>
        <text>Вот она какая, красная планета!</text>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
