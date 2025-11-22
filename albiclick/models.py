from datetime import datetime
from  albiclick import database


class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(250), nullable=False)
    email = database.Column(database.String(250), nullable=False)
    telefone = database.Column(database.String(250), nullable=False)
    mensagem = database.Column(database.Text, nullable=False)
    data_envio = database.Column(database.DateTime, default=datetime.utcnow)

