from models.metrics_model import  Metric
from app import db

def get_all_metrics():
    metrics = Metric.query.all()
    metric_list = []
    for metric in metrics:
        metric_data = {
            'event_uuid': metric.event_uuid,
            'event_time': metric.event_time.strftime('%Y-%m-%d %H:%M:%S'),
            'site_id': metric.site_id,
            'storage_gb': metric.storage_gb,
            'disc_cache': metric.disc_cache,
            'disc_a_gb': metric.disc_a_gb,
            'disc_b_gb': metric.disc_b_gb,
            'cpu_percent': metric.cpu_percent,
            'cpu_tic': metric.cpu_tic
        }
        metric_list.append(metric_data)
    return metric_list
