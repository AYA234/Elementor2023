from flask_sqlalchemy import SQLAlchemy
from app import db

class PackageToUser(db.Model):
    __tablename__ = 'packages_to_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    package_id = db.Column(db.Integer, db.ForeignKey('packages.package_id'))

    def __init__(self, user_id, package_id):
        self.user_id = user_id
        self.package_id = package_id
