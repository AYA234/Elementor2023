from models.usage_per_site_model import db, UsagePerSite

def get_all_usage_per_site(site_id):
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
