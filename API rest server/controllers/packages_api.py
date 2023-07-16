from flask import Blueprint, jsonify
from dal.packages_dal import get_all_packages

packages_api = Blueprint('packages_api', __name__)

@packages_api.route('/packages', methods=['GET'])
def get_packages():
    packages = get_all_packages()
    return jsonify(packages)



