from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>Миссия Колонизация Марса</h1>
                  </body>
                </html>"""


@app.route('/index')
def index():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация Марса</title>
                  </head>
                  <body>
                    <h1>И на Марсе будут яблони цвести!</h1>
                  </body>
                </html>"""


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Рекламная кампания</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.</h1>
                    <h1>Человечеству мала одна планета.</h1>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                    <h1>И начнем с Марса!</h1>
                    <h1>Присоединяйся!</h1>
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src='/static/img/mars.png' /img>
                    <br> <text> Вот она какая, красная планета. </text> </br>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
