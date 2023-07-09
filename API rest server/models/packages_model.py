from flask_sqlalchemy import SQLAlchemy
from app import db

class Package(db.Model):
    __tablename__ = 'packages'
    package_id = db.Column(db.Integer, primary_key=True)
    cost_per_month = db.Column(db.Integer)
    storage_gb = db.Column(db.Float)
    disc_cache = db.Column(db.Float)
    disc_a_gb = db.Column(db.Float)
    disc_b_gb = db.Column(db.Float)
    cpu_percent = db.Column(db.Float)
    cpu_tic = db.Column(db.Float)

    def __init__(self, package_id, cost_per_month, storage_gb, disc_cache, disc_a_gb, disc_b_gb, cpu_percent, cpu_tic):
        self.package_id = package_id
        self.cost_per_month = cost_per_month
        self.storage_gb = storage_gb
        self.disc_cache = disc_cache
        self.disc_a_gb = disc_a_gb
        self.disc_b_gb = disc_b_gb
        self.cpu_percent = cpu_percent
        self.cpu_tic = cpu_tic
