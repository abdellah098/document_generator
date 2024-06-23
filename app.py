
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./document_gen.db'
  db.init_app(app=app)
  from routes import register_routes
  register_routes(app=app, db=db)

  migrate = Migrate(app=app, db=db)
  return app