from flask_sqlalchemy import SQLAlchemy

from app import db

class Site(db.Model):
    __tablename__ = 'sites'
    site_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self, user_id):
        self.user_id = user_id
