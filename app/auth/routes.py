from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User
from . import auth_bp


@auth_bp.route('/login', methods=['GET'])
def login_form():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
    return render_template('login.html')


@auth_bp.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
    
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        flash('Missing username or password', 'error')
        return redirect(url_for('auth.login'))

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        flash('Invalid credentials', 'error')
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('dashboard.dashboard'))
    

@auth_bp.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')


@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return {'error': 'Missing username or password'}, 400

    user = User.query.filter_by(username=username).first()
    if user:
        return {'error': 'User already exists'}, 400

    user = User(username=username)
    user.set_password(password)
    user.save()

    login_user(user)
    return redirect(url_for('dashboard.dashboard'))


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))