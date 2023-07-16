from models.sites_to_package_model import db, SiteToPackage

def get_all_sites_to_packages():
    sites_to_packages = SiteToPackage.query.all()
    site_to_package_list = []
    for site_to_package in sites_to_packages:
        site_to_package_data = {
            'id': site_to_package.id,
            'package_id': site_to_package.package_id,
            'site_id': site_to_package.site_id
        }
        site_to_package_list.append(site_to_package_data)
    return site_to_package_list

def get_sites_to_package_by_package_id(package_id):

    sites_to_packages = SiteToPackage.query.filter(package_id=package_id).all()
    site_to_package_list = []
    for site_to_package in sites_to_packages:
        site_to_package_data = {
            'id': site_to_package.id,
            'package_id': site_to_package.package_id,
            'site_id': site_to_package.site_id
        }
        site_to_package_list.append(site_to_package_data)
    return site_to_package_list