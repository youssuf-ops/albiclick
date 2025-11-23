from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, length, Length


class FormContacto(FlaskForm):
    username = StringField('Nome Completo', validators=[DataRequired(),length(min=2,max=100)], render_kw={'placeholder': 'Digite seu nome'})
    email = StringField('Email Profissional', validators=[DataRequired(), Email()], render_kw={'placeholder': 'nome@empresa.com'})
    telefone = StringField('Contacto telefónico', validators=[DataRequired(), length(min=9, max=15)], render_kw={'placeholder': 'ex: +351 912 345 678'})
    mensagem = TextAreaField('Como posso ajudar?', validators=[DataRequired(), length(min=10, max=500)], render_kw={'placeholder': 'Descreva brevemente o que pretende (ex: dashboard, análise, estudo de mercado…)'})
    botao_submit_contacto = SubmitField('Enviar Mensagem')

