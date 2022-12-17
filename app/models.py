from datetime import datetime
from app import db
from flask_login import UserMixin

class Votes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_app.id'))
    def __repr__(self) -> str:
        return f"Vote registered in survey {self.survey_id} by user {self.user_id}"

class Option(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(10000))
    votes = db.Column(db.Integer)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    def __repr__(self) -> str:
        return f"Option {self.id} {self.text}, votes = {self.votes}"

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(10000))
    timestamp = db.Column(db.DateTime(timezone=True), index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_app.id'))   
    options = db.relationship('Option')
    voters = db.relationship('Votes')

    def __repr__(self) -> str:
        return f"Survey {self.id} {self.question}"

class User_app(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    surveys = db.relationship('Survey')

    def __repr__(self) -> str:
        return f"User {self.name}"