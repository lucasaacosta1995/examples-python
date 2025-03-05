from flask import Blueprint, render_template, request, redirect, url_for
from models.user import User

user_routes = Blueprint('user_routes', __name__)

# Ruta para listar todos los usuarios
@user_routes.route('/')
def index():
    users = User.get_all_users()
    return render_template('index.html', users=users)

# Ruta para agregar un nuevo usuario
@user_routes.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        User.create_user(nombre, email)
        return redirect(url_for('user_routes.index'))
    return render_template('edit_user.html', action="Agregar")

# Ruta para editar un usuario
@user_routes.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        User.update_user(id, nombre, email)
        return redirect(url_for('user_routes.index'))
    
    user = User.get_user_by_id(id)
    return render_template('edit_user.html', action="Editar", user=user)

# Ruta para eliminar un usuario
@user_routes.route('/delete/<int:id>', methods=['GET'])
def delete_user(id):
    User.delete_user(id)
    return redirect(url_for('user_routes.index'))
