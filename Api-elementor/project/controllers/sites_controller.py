from flask import Blueprint, jsonify
from dal import sites_dal

sites_controller = Blueprint('site_controller', __name__)

@sites_controller.route('/getAllSites', methods=['GET'])
def get_sites():
    sites = sites_dal.get_all_sites()
    site_list = []
    for site in sites:
        site_data = {
            'site_id': site.site_id,
            'user_id': site.user_id,
            'site_description':site.site_description,
            'site_name':site.site_name
        }
        site_list.append(site_data)
    return jsonify(site_list)

@sites_controller.route('/getSiteBySitId/<int:site_id>', methods=['GET'])
def get_site_by_site_id(site_id):
    site = sites_dal.get_site_by_site_id(site_id)
    site_data = {
            'site_id': site.site_id,
            'user_id': site.user_id,
            'site_description':site.site_description,
            'site_name':site.site_name
        }
    return jsonify(site_data)


