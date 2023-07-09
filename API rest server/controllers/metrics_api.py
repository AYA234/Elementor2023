from flask import Blueprint, jsonify
from dal.metrics_dal import get_all_metrics

metrics_api = Blueprint('metrics_api', __name__)

@metrics_api.route('/metrics', methods=['GET'])
def get_metrics():
    metrics = get_all_metrics()
    return jsonify(metrics)
