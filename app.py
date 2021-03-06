from flask_restless import APIManager
from flask import Flask, g
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = APIManager(app, flask_sqlalchemy_db=db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)
login_manager.login_view = "login"


@app.before_request
def _before_request():
    g.user = current_user