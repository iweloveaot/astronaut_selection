from flask import Flask, url_for

app = Flask(__name__)


@app.route('/astronaut_selection')
def form():
    return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1>Анкета претендента на участие в миссии</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="name" aria-describedby="neme" placeholder="Введите имя" name="name">
                                        <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее общее</option>
                                              <option>Среднее специальное</option>
                                              <option>Высшее</option>
                                            </select>
                                          </div>
                                        <div class="form-group">
                                            <label for="form-check">Какие у Вас есть профессии?</label>
                                            <div class="form-check">
                                              <input type="checkbox" class="form-check-input" id="explore" name="explorer">
                                              <label class="form-check-label" for="explore">Инженер-исследователь</label>
                                              </br><input type="checkbox" class="form-check-input" id="build" name="builder">
                                              <label class="form-check-label" for="build">Инженер-строитель</label>
                                              </br><input type="checkbox" class="form-check-input" id="pilot" name="pilot">
                                              <label class="form-check-label" for="pilot">Пилот</label>
                                              </br><input type="checkbox" class="form-check-input" id="meteo" name="meteo">
                                              <label class="form-check-label" for="meteo">Метеоролог</label>
                                              </br><input type="checkbox" class="form-check-input" id="life" name="lifer">
                                              <label class="form-check-label" for="life">Инженер по жизнеобеспечению</label>
                                              </br><input type="checkbox" class="form-check-input" id="uran" name="uran">
                                              <label class="form-check-label" for="uran">Инженер по радиационной защите</label>
                                              </br><input type="checkbox" class="form-check-input" id="doctor" name="doctor">
                                              <label class="form-check-label" for="doctor">Врач</label>
                                              </br><input type="checkbox" class="form-check-input" id="akzo" name="ekzo">
                                              <label class="form-check-label" for="akzo">Экзобиолог</label>
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
                                            <label>Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" rows="5"></textarea>
                                          </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                          </div>
                                        <div class="form-group">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Вы готовы остаться на Марсе?</label>
                                          </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')