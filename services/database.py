from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_database(app: Flask):
    try:
        engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
        if not database_exists(engine.url):
            create_database(engine.url)
        db.init_app(app)
        Migrate(app, db)
        db.create_all(app=app)
    except Exception as e:
        return str(e)