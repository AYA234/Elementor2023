from flask_sqlalchemy import SQLAlchemy
from app import db


class UsagePerSite(db.Model):
    __tablename__ = 'usage_per_site'
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.site_id'))
    time = db.Column(db.TIMESTAMP(timezone=True))
    storage_gb = db.Column(db.Float)
    disc_cache = db.Column(db.Float)
    disc_a_gb = db.Column(db.Float)
    disc_b_gb = db.Column(db.Float)
    cpu_percent = db.Column(db.Float)
    cpu_tic = db.Column(db.Float)

    def __init__(self, site_id, time, storage_gb, disc_cache, disc_a_gb, disc_b_gb, cpu_percent, cpu_tic):
        self.site_id = site_id
        self.time = time
        self.storage_gb = storage_gb
        self.disc_cache = disc_cache
        self.disc_a_gb = disc_a_gb
        self.disc_b_gb = disc_b_gb
        self.cpu_percent = cpu_percent
        self.cpu_tic = cpu_tic
