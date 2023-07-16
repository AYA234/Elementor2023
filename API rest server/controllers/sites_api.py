from flask import Blueprint, jsonify
from dal.site_dal import SiteDAL

site_api = Blueprint('site_api', __name__)

@site_api.route('/sites', methods=['GET'])
def get_sites():
    sites = SiteDAL.get_all_sites()
    site_list = []
    for site in sites:
        site_data = {
            'site_id': site.site_id,
            'user_id': site.user_id
        }
        site_list.append(site_data)
    return jsonify(site_list)
