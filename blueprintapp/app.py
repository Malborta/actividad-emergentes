from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    # CONFIGURACIÓN
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secretkey'

    # INICIALIZAR DB
    db.init_app(app)

    # IMPORTAR BLUEPRINT
    from blueprintapp.routes import main

    # REGISTRAR BLUEPRINT
    app.register_blueprint(main)

    # CREAR BASE DE DATOS
    with app.app_context():
        db.create_all()

    return app