from flask import Flask, url_for, request

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


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                    <html lang="ru">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                        <title>Колонизация!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <picture>
                        <img src="{url_for('static', filename='img/mars.jpg')}" class="img-fluid img-thumbnail" alt="image not found">
                        </picture>
                        <div class="alert alert-secondary" role="alert">
                        Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                        И начнем с Марса.
                        </div>
                        <div class="alert alert-danger" role="alert">
                        Присоединяйся.
                        </div>
                      </body>
                    </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                            <title>Запись в космонавты</title>
                          </head>
                          <body>
                            <h1>Анкета претендента на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post"  >
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="mail" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="educationForm" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее полное</option>
                                          <option>Среднее неполное</option>
                                          <option>Высшее техническое</option>
                                          <option>Высшее гуманитарное</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите Вашу основную профессию</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="engineer-explorer" value="engineer-explorer">
                                          <label class="form-check-label" for="engineer-explorer">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="pilot" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="biologist" value="biologist">
                                          <label class="form-check-label" for="biologist">
                                            Биолог
                                          </label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="doctor" value="doctor">
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="profession" id="meteorologist" value="meteorologist">
                                          <label class="form-check-label" for="meteorologist">
                                        Метеоролог
                                          </label>
                                        </div>          
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы решили принять участие в миссии?</label>
                                        <textarea class="form-control" id="goal" rows="3" name="goal"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Вы готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['goal'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(request.form['file'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
