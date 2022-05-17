from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app=Flask(__name__)
    
    import config
    app.config.from_object(config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    
    from .views import main
    app.register_blueprint(main.bp)
    
    return app