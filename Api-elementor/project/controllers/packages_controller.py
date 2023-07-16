from dal import packages_dal
from flask import Blueprint, jsonify


packages_controller = Blueprint('packages_api', __name__)
@packages_controller.route('/getAllPackages', methods=['GET'])
def get_packages():
    packages = packages_dal.get_all_packages()
    
    return jsonify(packages)

@packages_controller.route('/getPackageDetailsByPackageId/<int:package_id>')
def get_package_details_by_package_id(package_id):
    package_details=packages_dal.get_package_details_by_package_id(package_id)
    return jsonify(package_details)

@packages_controller.route('/getPackagesDetailsByPackageIds/<package_ids>')
def get_package_details_by_package_ids(package_ids):
    pacakes_detils=[]
    for package_id in package_ids:
        pacakes_detils.append(packages_dal.get_package_details_by_package_id(package_id))
    return jsonify(pacakes_detils)