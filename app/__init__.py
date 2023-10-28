from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO, send, emit

import app.routes as routes

db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.secret_key = 'doggietroll' 
    login_manager.init_app(app)
    db.init_app(app)

    app.config['access_log'] = True

    socketio = SocketIO(app, cors_allowed_origins="*")

    from app.models import User
    from app.models import Guest
    

    routes.configure_routes(app, db, login_manager, socketio)

    from api.api_routes import configure_api_routes

    configure_api_routes(app, db, login_manager, socketio)
    
    return app, db, socketio
