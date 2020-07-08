from flask import Flask, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
FLASK_APP = app
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'cachorros.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)