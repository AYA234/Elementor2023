from flask import Blueprint, jsonify
from dal import metrics_dal

metrics_controller = Blueprint('metrics_api', __name__)

@metrics_controller.route('/getAllMetrics', methods=['GET'])
def get_metrics():
    metrics = metrics_dal.get_all_metrics()
    return jsonify(metrics)
