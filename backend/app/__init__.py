from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from backend.app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    CORS(app)
    
    # Register blueprints
    from backend.app.routes.auth import auth_bp
    from backend.app.routes.feed import feed_bp
    from backend.app.routes.events import events_bp
    from backend.app.routes.study_buddy import study_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(feed_bp, url_prefix='/api/feed')
    app.register_blueprint(events_bp, url_prefix='/api/events')
    app.register_blueprint(study_bp, url_prefix='/api/study')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
