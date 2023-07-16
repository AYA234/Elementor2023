from models.packages_model import Package
from app import db
def get_all_packages():
    packages = Package.query.all()
    package_list = []
    for package in packages:
        package_data = {
            'package_id': package.package_id,
            'cost_per_month': package.cost_per_month,
            'storage_gb': package.storage_gb,
            'disc_cache': package.disc_cache,
            'disc_a_gb': package.disc_a_gb,
            'disc_b_gb': package.disc_b_gb,
            'cpu_percent': package.cpu_percent,
            'cpu_tic': package.cpu_tic
        }
        package_list.append(package_data)
    return package_list
