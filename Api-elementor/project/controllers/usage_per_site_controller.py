from flask import Blueprint, jsonify
from dal import usage_per_site_dal

usage_per_site_controller = Blueprint('usage_per_site_controller', __name__)

@usage_per_site_controller.route('/getLastUsages/<int:site_id>/<int:number_of_last_usages>', methods=['GET'])
def get_last_usages(site_id,number_of_last_usages):
    usage_per_site_list = usage_per_site_dal.get_last_usages(site_id,number_of_last_usages)
    # /
    usage_per_site_list = [
    {
        "cpu_percent": 70.3,
        "cpu_tic": 250.0,
        "disc_a_gb": 15.8,
        "disc_b_gb": 25.0,
        "disc_cache": 5.7,
        "id": 2,
        "site_id": 2,
        "storage_gb": 100.2,
        "time": "2023-01-13 11:31:16"
    },
    {
        "cpu_percent": 80,
        "cpu_tic": 300,
        "disc_a_gb": 20,
        "disc_b_gb": 30,
        "disc_cache": 6,
        "id": 2,
        "site_id": 2,
        "storage_gb": 150,
        "time": "2023-02-13 11:31:16"
    },
    {
        "cpu_percent": 70.3,
        "cpu_tic": 250.0,
        "disc_a_gb": 15.8,
        "disc_b_gb": 25.0,
        "disc_cache": 5.7,
        "id": 2,
        "site_id": 2,
        "storage_gb": 100.2,
        "time": "2023-03-13 11:31:16"
    },
    {
        "cpu_percent": 150,
        "cpu_tic": 400,
        "disc_a_gb": 60,
        "disc_b_gb": 251,
        "disc_cache": 66,
        "id": 2,
        "site_id": 2,
        "storage_gb": 99,
        "time": "2023-05-13 11:31:16"
    },
    {
        "cpu_percent": 70.3,
        "cpu_tic": 250.0,
        "disc_a_gb": 15.8,
        "disc_b_gb": 25.0,
        "disc_cache": 5.7,
        "id": 2,
        "site_id": 2,
        "storage_gb": 100.2,
        "time": "2023-06-13 11:31:16"
    },
    {
        "cpu_percent": 7,
        "cpu_tic": 25,
        "disc_a_gb": 1,
        "disc_b_gb": 2,
        "disc_cache": 5,
        "id": 2,
        "site_id": 2,
        "storage_gb": 10,
        "time": "2023-07-13 11:31:16"
    },
    {
        "cpu_percent": 70.3,
        "cpu_tic": 250.0,
        "disc_a_gb": 15.8,
        "disc_b_gb": 25.0,
        "disc_cache": 5.7,
        "id": 2,
        "site_id": 2,
        "storage_gb": 100.2,
        "time": "2023-08-13 11:31:16"
    }
]
    # /
    return jsonify(usage_per_site_list)

@usage_per_site_controller.route('/getTotalPackageUsage/<int:package_id>', methods=['GET'])
def get_total_package_usage(package_id):
    total_package_usage = usage_per_site_dal.get_total_package_usage(package_id)
    return jsonify(total_package_usage)

