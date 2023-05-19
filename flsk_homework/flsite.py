from flask import Flask, render_template, url_for, request, flash, session, g, redirect
import os
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dflkhdflijhlfdjyhgfyujhfghkhgkghkghfghgfhlgk'
app.config.from_object(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "Страны", "url": "country"},
    {"name": "О компании", "url": "company"},
    {"name": "Акции и туры", "url": "stock"},
    {"name": "Контакты", "url": "contact"},
]


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title="Главная", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


@app.route("/country")
def country():
    return render_template('country.html', title="Страны", menu=menu)


@app.route("/company")
def company():
    return render_template('company.html', title="О компании", menu=menu)


@app.route("/stock")
def stock():
    return render_template('stock.html', title="Акции и туры", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['message']) > 2:
            flash('Сообщение отправлено успешно', category='success')
        else:
            flash('Ошибка отправки', category='error')
        context = {
            'username': request.form['username'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        return render_template('contact.html', title="Контакты", menu=menu, **context)
    return render_template('contact.html', title="Контакты", menu=menu)


@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'nadia' and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title="Авторизация", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)


