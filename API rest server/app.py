from flask import Flask
from flask_sqlalchemy import SQLAlchemy

host = "test-rds-dev.colcjtm9obot.eu-west-1.rds.amazonaws.com"
port = 5432
database = "metrics_dev"
user = "developer"
password = "41b387c1-2cf9-4436-85fa-7c75093b7d14"

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the SQLAlchemy instance with the app
    db.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    # Import the API blueprints here to avoid circular imports
    from api.packages_to_users_api import packages_to_users_api
    from api.packages_api import packages_api
    from api.metrics_api import metrics_api
    from api.sites_api import site_api
    from api.sites_to_package_api import sites_to_package_api
    from api.user_api import user_api
    # from api.usage_per_site_api import usage_per_site_api

    # Register the API blueprints
    app.register_blueprint(packages_to_users_api)
    # app.register_blueprint(usage_per_site_api)
    app.register_blueprint(user_api)
    app.register_blueprint(site_api)
    app.register_blueprint(metrics_api)
    app.register_blueprint(packages_api)
    app.register_blueprint(sites_to_package_api)

    with app.app_context():
        db.create_all()

    app.run()
