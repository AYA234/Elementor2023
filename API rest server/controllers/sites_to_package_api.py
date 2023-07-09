from flask import Blueprint, jsonify
from dal.sites_to_package_model import get_all_sites_to_packages,get_sites_to_package_by_package_id

sites_to_package_api = Blueprint('sites_to_package_api', __name__)

@sites_to_package_api.route('/getAllSitesToPackages', methods=['GET'])
def get_all_sites_to_packages():
    sites_to_packages = get_all_sites_to_packages()
    return jsonify(sites_to_packages)


@sites_to_package_api.route('/getSitesToPackageByPackageId/<int:package_id>', methods=['GET'])
def get_sites_to_package_by_package_id(package_id):
    sites_to_packages = get_sites_to_package_by_package_id(package_id)
    return jsonify(sites_to_packages)

