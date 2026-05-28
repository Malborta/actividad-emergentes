from blueprintapp.app import db

class Datos(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100), nullable=False)