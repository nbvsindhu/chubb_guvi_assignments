from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class ClimateData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Float)
    precipitation = db.Column(db.Float)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<ClimateData {self.source} on {self.date}>'
