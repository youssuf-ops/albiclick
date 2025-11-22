from flask import Flask, render_template, request, redirect, url_for, flash
from  albiclick import app, database

from albiclick.forms import FormContacto
from albiclick.models import Usuario

# -- Definição de rotas ---

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/contacto', methods=['GET','POST'])
def contacto():
    form_contacto = FormContacto()

    if form_contacto.validate_on_submit():

        novo = Usuario(
            username=form_contacto.username.data,
            email=form_contacto.email.data,
            telefone=form_contacto.telefone.data,
            mensagem=form_contacto.mensagem.data
        )

        database.session.add(novo)
        database.session.commit()

        flash('Contacto recebido com sucesso. Responderei o mais rápido possível.', 'success')
        return redirect(url_for('hello_world'))

    return render_template('contacto.html', form_contacto=form_contacto)


@app.route('/privacidade')
def privacidade():
    return render_template('privacidade.html')