from flask import Blueprint, jsonify
from dal import sites_to_package_dal
sites_to_package_controller = Blueprint('sites_to_package_controller', __name__)

@sites_to_package_controller.route('/getAllSitesToPackages', methods=['GET'])
def get_all_sites_to_packages():
    sites_to_packages = sites_to_package_dal.get_all_sites_to_packages()
    return jsonify(sites_to_packages)


@sites_to_package_controller.route('/getSitesToPackageByPackageId/<int:package_id>', methods=['GET'])
def get_sites_to_package_by_package_id(package_id):
    sites_to_packages = sites_to_package_dal.get_sites_to_package_by_package_id(package_id)
    return jsonify(sites_to_packages)




