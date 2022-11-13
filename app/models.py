from datetime import datetime
from app import db
from flask_login import UserMixin

class Option(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(10000))
    votes = db.Column(db.Integer)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(10000))
    timestamp = db.Column(db.DateTime(timezone=True), index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   
    options = db.relationship('Option')

    def __repr__(self) -> str:
        return f"Survey {self.id} {self.question}"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notes = db.relationship('Survey')

    def __repr__(self) -> str:
        return f"User {self.name}"