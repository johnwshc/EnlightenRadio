from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "you will never gue55"
from app import routes