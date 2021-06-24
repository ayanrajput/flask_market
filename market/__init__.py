from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///market.db"
app.config["SECRET_KEY"]='ca7c566aef335679b5b41087'
db=SQLAlchemy(app)

from market import routes
