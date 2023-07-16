
from flask import Flask
from flask_cors import CORS
from models.db_model import db


from controllers.packages_to_users_controller import packages_to_users_controller
from controllers.packages_controller import packages_controller
from controllers.metrics_controller import metrics_controller
from controllers.sites_controller import sites_controller
from controllers.sites_to_package_controller import sites_to_package_controller
from controllers.user_controller import users_controller
from controllers.usage_per_site_controller import usage_per_site_controller


host = "test-rds-dev.colcjtm9obot.eu-west-1.rds.amazonaws.com"
port = 5432
database = "metrics_dev"
user = "developer"
password = "41b387c1-2cf9-4436-85fa-7c75093b7d14"



def create_app():

    app = Flask(__name__)

    # SQLAlchemy configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    cors = CORS(app)


    # Database connection
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # Register API blueprints

   
    app.register_blueprint(packages_to_users_controller)
    app.register_blueprint(usage_per_site_controller)
    app.register_blueprint(users_controller)
    app.register_blueprint(sites_controller)
    app.register_blueprint(metrics_controller)
    app.register_blueprint(packages_controller)
    app.register_blueprint(sites_to_package_controller)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
