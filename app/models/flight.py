from app.db import db

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    month = db.Column(db.SmallInteger)
    market = db.Column(db.Integer, db.ForeignKey('market.id'))
    rpk = db.Column(db.Double)