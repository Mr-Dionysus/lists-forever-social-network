from os import getenv

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql+psycopg2://{getenv('DB_LOGIN')}:{getenv('DB_PASS')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_DATABASE')}"
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from lists_forever import models, views
