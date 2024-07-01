# app/routes.py

from flask import render_template, request, redirect, url_for, flash
from flask_mail import Message
from app import app, mail
from app.forms import LoginForm, RegisterForm

# Exemplo de rota para página inicial
@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

# Rota para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Lógica de verificação de login aqui (exemplo básico)
        flash(f'Login requested for user {form.username.data}', 'info')
        return redirect(url_for('use_file'))
    return render_template('login.html', form=form)

# Rota para registro de novo usuário
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Lógica de criação de conta aqui (exemplo básico)
        flash(f'Account created for {form.username.data}. Please check your email for confirmation.', 'success')
        # Enviar e-mail de confirmação
        send_confirmation_email(form.email.data)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Rota para página protegida (exige login)
@app.route('/use_file')
def use_file():
    # Lógica para verificar se o usuário está logado
    # Implemente a lógica de sessão de usuário ou login aqui
    return render_template('use_file.html')

# Função para enviar e-mail de confirmação
def send_confirmation_email(email):
    msg = Message('Confirm Your Email', sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[email])
    # Conteúdo do e-mail
    msg.body = 'Please confirm your email by clicking on the link below:'
    # Envie o e-mail
    mail.send(msg)
