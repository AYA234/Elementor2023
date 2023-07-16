from models.sites_model import Site


def get_all_sites():
    sites = Site.query.all()
    return sites

def get_site_by_site_id(site_id):
    site=Site.query.filter(Site.site_id==site_id).first()
    return site