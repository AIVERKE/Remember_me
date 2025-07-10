from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@login_required
def home():
    return render_template('home.html', usenamername=current_user.name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        remember = True if request.form.get('remember') == 'on' else False

        user = User.query.filter_by(name=name).first()

        if user:
            print("Nombre:", user.name)
            print("Contraseña:", user.password)
        else:
            print("No se encontró usuario:", name)

        if user and user.password == password:
            login_user(user, remember=remember)
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos')


    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
