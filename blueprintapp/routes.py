from flask import Blueprint, render_template, request, redirect, url_for
from blueprintapp.app import db
from blueprintapp.models import Datos

main = Blueprint('main', __name__)

# INICIO
@main.route('/')
def index():

    datos = Datos.query.all()

    return render_template('index.html', datos=datos)

# NUEVO
@main.route('/nuevo', methods=['GET', 'POST'])
def nuevo():

    if request.method == 'POST':

        nombre = request.form['nombre']

        nuevo_dato = Datos(nombre=nombre)

        db.session.add(nuevo_dato)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('nuevo.html')

# EDITAR
@main.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    registro = Datos.query.get_or_404(id)

    if request.method == 'POST':

        registro.nombre = request.form['nombre']

        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('editar.html', registro=registro)

# ELIMINAR
@main.route('/eliminar/<int:id>')
def eliminar(id):

    registro = Datos.query.get_or_404(id)

    db.session.delete(registro)

    db.session.commit()

    return redirect(url_for('main.index'))