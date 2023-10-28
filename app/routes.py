from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user, login_user
from werkzeug.security import check_password_hash

def configure_routes(app, db, login_manager, socketio):
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html', current_user=current_user)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        
        return render_template('register.html', current_user=current_user)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        
        return render_template('login.html', current_user=current_user)
    
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('auth'))