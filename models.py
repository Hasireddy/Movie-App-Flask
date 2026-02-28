from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#User model

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)



#Movie model

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    director = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)