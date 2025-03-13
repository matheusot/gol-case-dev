from app.db import db

class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    market = db.Column(db.String(8))