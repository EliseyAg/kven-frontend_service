from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import os
import sys
from datetime import timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from config import Config
from utils.api_client import APIClient
from utils.session import SessionManager


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY

app.permanent_session_lifetime = timedelta(hours=1)


@app.route('/')
def index():
    return redirect("/feed")


@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('feed'))
        return render_template('auth/login.html')

        # POST: обработка логина
    username_or_email = request.form.get('username_or_email')
    password = request.form.get('password')

    if not username_or_email or not password:
        flash('Please fill all fields', 'error')
        return render_template('auth/login.html'), 400

    # Вызываем Auth Service через API клиент
    try:
        response = api_client.login(username_or_email, password)

        if response.get('access_token'):
            # Сохраняем токены в сессии
            session['access_token'] = response['access_token']
            session['refresh_token'] = response['refresh_token']
            session['user'] = response['user']
            session.permanent = True

            flash('Login successful!', 'success')
            return redirect(url_for('feed'))
        else:
            flash('Invalid credentials', 'error')
            return render_template('auth/login.html'), 401

    except Exception as e:
        flash(f'Login error: {str(e)}', 'error')
        return render_template('auth/login.html'), 500
