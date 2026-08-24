# Importações de bibliotecas e ferramentas necessárias
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime # Importa ferramentas para manipulação de data, hora e intervalos de tempo

# Inicialização de Flask e definição de chave secreta
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Chave Forte'

bootstrap = Bootstrap(app)
moment = Moment(app) # Flask-Moment para exibir o tempo decorrido de forma dinâmica -->

# Criação do formulário e suas definições
class NameForm(FlaskForm):
  name = StringField('Informe o seu nome:', validators= [DataRequired()])
  surname = StringField('Informe o seu sobrenome:', validators= [DataRequired()])
  institution = StringField('Informe a sua instituição de ensino:', validators= [DataRequired()])
  discipline = SelectField('Informe a sua disciplina:', choices=[
        ('DSWS4', 'DSWS4'),
        ('DSWS5', 'DSWS5'),
        ('Gestao', 'Gestao de Projetos'),
        ('BD', 'Banco de Dados')
  ])
  submit = SubmitField('Enviar')

# Rota função view
@app.route('/', methods=['GET', 'POST'])
def index():

    ip_remoto = request.remote_addr
    host_aplicacao = request.host

    # Captura do ip e host com a variável especial request
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name'), # antes da primeira submissão
        old_surname = session.get('surname'),
        old_institution = session.get('institution'),
        old_discipline = session.get('discipline')

        # Validação do envio do formulário (PRG)
        if old_name is not None and old_name != form.name.data:
            flash('Nome alterado com sucesso!')

        if old_surname is not None and old_surname != form.surname.data:
            flash('Sobrenome alterado com sucesso!')

        if old_institution is not None and old_institution != form.institution.data:
            flash('Instituição atualizada com sucesso!')

        if old_discipline is not None and old_discipline != form.discipline.data:
            flash('Disciplina alterada com sucesso!')

        # Save dos dados na session
        session['name'] = form.name.data # variável de sessão
        session['surname'] = form.surname.data
        session['institution'] = form.institution.data
        session['discipline'] = form.discipline.data

        return redirect(url_for('index')) #salva na session e redireciona para a rota index

    # Cálculo do tempo decorrido
    now = datetime.now()
    formatted_time = now.strftime("%B %d, %Y %I:%M %p")

    # Renderiza a página HTML com os dados salvos na session
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           surname=session.get('surname'),
                           institution=session.get('institution'),
                           discipline=session.get('discipline'),
                           ip=ip_remoto,
                           host=host_aplicacao,
                           current_time=formatted_time,  # envia para o html
                           moment_time=now)

# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    now = datetime.now() # horário atual
    formatted_time = now.strftime("%B %d, %Y %I:%M %p") # formatação de data e hora

    return render_template('login.html',
                           current_time=formatted_time,
                           moment_time=now)

if __name__ == '__main__': # verifica se o arquivo está sendo executado diretamente e inicia a aplicação web.
    app.run(debug=True) # reinicia o servidor automaticamente ao salvar alterações.