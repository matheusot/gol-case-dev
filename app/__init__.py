import os
from flask import Flask
from app.db import init_app, create_tables
from app.auth import auth_bp
from app.auth.login_manager import login_manager
from app.dashboard import dashboard_bp
from app.flights import flights_bp
from app.markets import markets_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.static_folder = 'static'

    init_app(app)
    create_tables(app)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    blueprints = (flights_bp, markets_bp, auth_bp, dashboard_bp)
    for bp in blueprints:
        app.register_blueprint(bp)

    return app