from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 

class Throwersd(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    year = db.Column(db.Integer)
    spbest=db.Column(db.Float)
    bp=db.Column(db.Integer)
    squat=db.Column(db.Integer)
    clean=db.Column(db.Integer)