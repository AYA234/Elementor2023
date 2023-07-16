from flask import Blueprint, jsonify
from dal import packages_to_users_dal,packages_dal,sites_to_package_dal
from models.packages_to_users_model import PackageToUser


packages_to_users_controller = Blueprint('packages_to_users_controller', __name__)

@packages_to_users_controller.route('/getAllPackagesToUsers', methods=['GET'])
def get_all_packages_to_users():
    all_package_to_users = packages_to_users_dal.get_all_packages_to_users()
    return jsonify(all_package_to_users)

@packages_to_users_controller.route('/getUserPackagesByUserId/<int:user_id>', methods=['GET'])
def get_user_packages(user_id):
    packages = packages_to_users_dal.get_user_packages(user_id)
    package_ids=[]
    for package in packages:
        package_ids.append(package.package_id)   
    package_details=[] 
    details={}
    for package_id in package_ids:
        details=packages_dal.get_package_details_by_package_id(package_id)
        sites=sites_to_package_dal.get_sites_to_package_by_package_id(package_id)
        details['sites_per_package']=sites
        package_details.append(details)
   
    return jsonify({'packages': package_details})



