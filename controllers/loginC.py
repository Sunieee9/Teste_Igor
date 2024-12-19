from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash
from repository import PersonRepository
from models.homeM import User

# Usuário administrador pré-configurado no código
admin_user = User("admin@gmail.com", "senhaforte", "admin")  # Usuário administrador
user_list = [admin_user]  # Lista de usuários pré-configurados

# Cria um blueprint
login_controller = Blueprint('login_controller', __name__)

# Define a rota para a página de login
@login_controller.route('/login', methods=['POST', 'GET'])
def login_page():

    if request.method == "POST":
        email = request.form['email']  # Obtém o email do formulário
        password = request.form['password']  # Obtém a senha do formulário

        # 1. Verifica se o usuário está na lista de usuários pré-configurados
        for user in user_list:
            if user.email == email and user.password == password:
                session['email_logado'] = user.email
                session['role'] = user.role
                flash(f'{user.email} está logado com sucesso!')

                # Redirecionamento com base no papel
                if user.role == 'admin':
                    return redirect(url_for('login_controller.admin_page'))
                else:
                    return redirect(url_for('login_controller.user_page'))

        # 2. Se não estiver na lista, busca no banco de dados
        person_repository = PersonRepository()
        person = person_repository.get_person_by_email(email)

        if person and person.password == password:
            session['email_logado'] = person.email
            session['role'] = person.access_level

            # Redirecionamento com base no papel
            if person.access_level == 'admin':
                return redirect(url_for('login_controller.admin_page'))
            else:
                return redirect(url_for('login_controller.user_page'))

        # Se nenhum usuário for validado
        flash('Usuário ou senha incorretos.')
        return redirect(url_for('login_controller.login_page'))

    # Renderiza a página de login se a requisição for GET
    return render_template('login.html')

# Define a rota para a página do administrador
@login_controller.route('/admin')
def admin_page():

    if 'email_logado' not in session or session.get('role') != 'admin':
        flash("Você precisa estar logado como administrador para acessar essa página.")
        return redirect(url_for('login_controller.login_page'))
    return render_template('admin.html')

# Define a rota para a página do usuário comum
@login_controller.route('/user')
def user_page():

    if 'email_logado' not in session:
        flash("Você precisa estar logado para acessar essa página.")
        return redirect(url_for('login_controller.login_page'))
    return render_template('user.html')

# Define a rota para o logout
@login_controller.route('/logout')
def logout():
    session.pop('email_logado', None)
    session.pop('role', None)
    flash("Você foi deslogado com sucesso.")
    return redirect(url_for('home.home'))
