from flask import Blueprint, jsonify,request
from dal.usage_per_site_api_dal_ import get_all_usage_per_site

usage_per_site_api = Blueprint('usage_per_site_api', __name__)


@usage_per_site_api.route('/getUserPerSite/<int:site_id>/<int:number_of_notations', methods=['POST'])
def get_usage_per_site(site_id):
    data = request.json
    number_of_notations = data.get('number_of_notations')
    usage_per_sites = get_all_usage_per_site(site_id, number_of_notations)
    return jsonify(usage_per_sites)

