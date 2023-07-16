from flask_sqlalchemy import SQLAlchemy
from models.db_model import db

class SiteToPackage(db.Model):
    __tablename__ = 'sites_to_package'
    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.package_id'))
    site_id = db.Column(db.Integer, db.ForeignKey('sites.site_id'))

    def __init__(self, package_id, site_id):
        self.package_id = package_id
        self.site_id = site_id
