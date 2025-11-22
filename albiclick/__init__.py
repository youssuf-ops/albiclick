from flask import Flask
#from albiclick.forms import FormContacto
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '489caf8c87efe7712d213ec32c355ce0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

database = SQLAlchemy(app)

#para que DB conheça as tabelas antes das rotas
from albiclick import models

#importaçao correta das rotas
from albiclick import routes
