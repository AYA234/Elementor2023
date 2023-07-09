from flask import Blueprint, jsonify
# from dal.packages_to_users_dal import get_all_packages_to_users
from models.packages_to_users_model import PackageToUser
from models.packages_model import Package
from models.sites_model import Site
from models.usage_per_site_model import UsagePerSite
from models.sites_to_package_model import SiteToPackage

packages_to_users_api = Blueprint('packages_to_users_api', __name__)

@packages_to_users_api.route('/packages_to_users', methods=['GET'])
def get_packages_to_users():
    print('usage')
    package_to_users = []#get_all_packages_to_users()
    return jsonify(package_to_users)

# @packages_to_users_api.route('/users/<int:user_id>/packages', methods=['GET'])
# def get_user_packages(user_id):
#     # Query the database to retrieve the user's packages
#     packages = PackageToUser.query\
#         .join(PackageToUser, PackageToUser.package_id == PackageToUser.package_id)\
#         .filter(PackageToUser.user_id == user_id)\
#         .all()

    
#     # Prepare the response data
#     package_list = []
#     for package in packages:
#         package_data = {
#             'package_id': package.package_id,
#             'cost_per_month': package.cost_per_month,
#             'storage_gb': package.storage_gb,
#             'disc_cache': package.disc_cache,
#             'disc_a_gb': package.disc_a_gb,
#             'disc_b_gb': package.disc_b_gb,
#             'cpu_percent': package.cpu_percent,
#             'cpu_tic': package.cpu_tic
#         }
#         package_list.append(package_data)

#     # Return the response
#     return jsonify({'packages': package_list})


# @packages_to_users_api.route('/getPackagesDetails/<int:user_id>/packages', methods=['GET'])
# def get_packages_details(user_id):
#     # Query the database to retrieve the user's packages
#     print('l')
#     packages = PackageToUser.query\
#         .join(Package, Package.package_id == PackageToUser.package_id)\
#         .filter(PackageToUser.user_id == user_id)\
#         .all()

#     # Prepare the response data
#     package_list = []
#     for package in packages:
#         package_data = {
#             'package_id': package.package.package_id,
#             'cost_per_month': package.package.cost_per_month,
#             'storage_gb': package.package.storage_gb,
#             'disc_cache': package.package.disc_cache,
#             'disc_a_gb': package.package.disc_a_gb,
#             'disc_b_gb': package.package.disc_b_gb,
#             'cpu_percent': package.package.cpu_percent,
#             'cpu_tic': package.package.cpu_tic,
#             'sites': {}
#         }

#         # Query the sites included in the package
#         sites = SiteToPackage.query\
#             .join(Site, Site.site_id == SiteToPackage.site_id)\
#             .filter(SiteToPackage.package_id == package.package.package_id)\
#             .all()

#         # Retrieve the usage data for each site
#         for site in sites:
#             usage = UsagePerSite.query\
#                 .filter(UsagePerSite.site_id == site.site.site_id)\
#                 .order_by(UsagePerSite.time.desc())\
#                 .first()

#             site_data = {
#                 'storage_gb': usage.storage_gb,
#                 'disc_cache': usage.disc_cache,
#                 'disc_a_gb': usage.disc_a_gb,
#                 'disc_b_gb': usage.disc_b_gb,
#                 'cpu_percent': usage.cpu_percent,
#                 'cpu_tic': usage.cpu_tic
#             }

#             package_data['sites'][site.site.site_id] = site_data

#         package_list.append(package_data)

#     # Return the response
#     return jsonify({'packages': package_list})



from flask import jsonify
from app import db
from models.packages_to_users_model import PackageToUser
from models.packages_model import Package
from models.sites_model import Site
from models.usage_per_site_model import UsagePerSite
from models.sites_to_package_model import SiteToPackage

@packages_to_users_api.route('/getPackagesDetails/<int:user_id>/packages', methods=['GET'])
def get_packages_details(user_id):
    # Query the database to retrieve the user's packages
    packages = PackageToUser.query\
        .join(Package, Package.package_id == PackageToUser.package_id)\
        .filter(PackageToUser.user_id == user_id)\
        .all()

    # Prepare the response data
    package_list = []
    for package in packages:
        package_data = {
            'package_id': package.package.package_id,
            'cost_per_month': package.package.cost_per_month,
            'storage_gb': package.package.storage_gb,
            'disc_cache': package.package.disc_cache,
            'disc_a_gb': package.package.disc_a_gb,
            'disc_b_gb': package.package.disc_b_gb,
            'cpu_percent': package.package.cpu_percent,
            'cpu_tic': package.package.cpu_tic,
            'sites': {}
        }

        # Query the sites included in the package
        # sites = SiteToPackage.query\
        #     .join(Site, Site.site_id == SiteToPackage.site_id)\
        #     .filter(SiteToPackage.package_id == package.package.package_id)\
        #     .all()

        # # Retrieve the usage data for each site
        # for site in sites:
        #     usage = UsagePerSite.query\
        #         .filter(UsagePerSite.site_id == site.site.site_id)\
        #         .order_by(UsagePerSite.time.desc())\
        #         .first()

        #     site_data = {
        #         'storage_gb': usage.storage_gb,
        #         'disc_cache': usage.disc_cache,
        #         'disc_a_gb': usage.disc_a_gb,
        #         'disc_b_gb': usage.disc_b_gb,
        #         'cpu_percent': usage.cpu_percent,
        #         'cpu_tic': usage.cpu_tic
        #     }

        #     package_data['sites'][site.site.site_id] = site_data

        # package_list.append(package_data)

    # Return the response
    return jsonify({'packages': package_data})
