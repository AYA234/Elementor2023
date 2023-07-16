from sqlalchemy import engine_from_config
from models.usage_per_site_model import  UsagePerSite
from models.sites_to_package_model import SiteToPackage
from dal.sites_to_package_dal import get_sites_to_package_by_package_id
from models.db_model import db



def get_all_usages_per_site(site_id):
    usage_per_sites = UsagePerSite.query.filter(site_id=site_id).all()
    usage_per_site_list = []
    for usage_per_site in usage_per_sites:
        usage_per_site_data = {
            'id': usage_per_site.id,
            'site_id': usage_per_site.site_id,
            'time': usage_per_site.time.strftime('%Y-%m-%d %H:%M:%S'),
            'storage_gb': usage_per_site.storage_gb,
            'disc_cache': usage_per_site.disc_cache,
            'disc_a_gb': usage_per_site.disc_a_gb,
            'disc_b_gb': usage_per_site.disc_b_gb,
            'cpu_percent': usage_per_site.cpu_percent,
            'cpu_tic': usage_per_site.cpu_tic
        }
        usage_per_site_list.append(usage_per_site_data)
    return usage_per_site_list


def get_last_usages(site_id,number_of_last_usages):
    usage_per_sites = UsagePerSite.query.filter_by(site_id=site_id).order_by(UsagePerSite.time.desc()).limit(number_of_last_usages).all()
    usage_per_site_list = []
    for usage_per_site in usage_per_sites:
        usage_per_site_data = {
            'id': usage_per_site.id,
            'site_id': usage_per_site.site_id,
            'time': usage_per_site.time.strftime('%Y-%m-%d %H:%M:%S'),
            'storage_gb': usage_per_site.storage_gb,
            'disc_cache': usage_per_site.disc_cache,
            'disc_a_gb': usage_per_site.disc_a_gb,
            'disc_b_gb': usage_per_site.disc_b_gb,
            'cpu_percent': usage_per_site.cpu_percent,
            'cpu_tic': usage_per_site.cpu_tic
        }
        usage_per_site_list.append(usage_per_site_data)
    return usage_per_site_list



def get_total_package_usage(package_id):
    sites=get_sites_to_package_by_package_id(package_id)
    site_ids=[s['site_id'] for s in sites]
    
    session = db.session
    results = session.query(UsagePerSite).filter(UsagePerSite.site_id.in_(site_ids)).all()

    total_storage_gb = 0.0
    total_disc_cache = 0.0
    total_disc_a_gb = 0.0
    total_disc_b_gb = 0.0
    total_cpu_percent = 0.0
    total_cpu_tic = 0.0

    for usage_per_site in results:
        total_storage_gb += usage_per_site.storage_gb
        total_disc_cache += usage_per_site.disc_cache
        total_disc_a_gb += usage_per_site.disc_a_gb
        total_disc_b_gb += usage_per_site.disc_b_gb
        total_cpu_percent += usage_per_site.cpu_percent
        total_cpu_tic += usage_per_site.cpu_tic

    total_usae_per_package = {
        'total_storage_gb': total_storage_gb,
        'total_disc_cache': total_disc_cache,
        'total_disc_a_gb': total_disc_a_gb,
        'total_disc_b_gb': total_disc_b_gb,
        'total_cpu_percent': total_cpu_percent,
        'total_cpu_tic': total_cpu_tic
    }
    

    return  total_usae_per_package
