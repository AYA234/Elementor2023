from app import db
from models.sites_model import Site

class SiteDAL:
    @staticmethod
    def get_all_sites():
        sites = Site.query.all()
        return sites
