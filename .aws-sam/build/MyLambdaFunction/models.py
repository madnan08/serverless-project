from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def _repr_(self):
        return f"User('{self.username}', '{self.email}')"
