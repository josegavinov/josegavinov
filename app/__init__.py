from flask import Flask
import os 
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'sqlite:///portafolio.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    db.init_app(app)

    from app.main import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        from app.models.project import Project 
        db.create_all()
    return app