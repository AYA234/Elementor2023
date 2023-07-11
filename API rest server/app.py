# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# host = "test-rds-dev.colcjtm9obot.eu-west-1.rds.amazonaws.com"
# port = 5432
# database = "metrics_dev"
# user = "developer"
# password = "41b387c1-2cf9-4436-85fa-7c75093b7d14"

# db = SQLAlchemy()


# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     # Initialize the SQLAlchemy instance with the app
#     db.init_app(app)

#     return app


# if __name__ == '__main__':
#     app = create_app()
#     # Import the API blueprints here to avoid circular imports
#     from controllers.packages_to_users_api import packages_to_users_api
#     from controllers.packages_api import packages_api
#     from controllers.metrics_api import metrics_api
#     from controllers.sites_api import site_api
#     from controllers.sites_to_package_api import sites_to_package_api
#     from controllers.user_api import user_api
#     # from api.usage_per_site_api import usage_per_site_api

#     # Register the API blueprints
#     app.register_blueprint(packages_to_users_api)
#     # app.register_blueprint(usage_per_site_api)
#     app.register_blueprint(user_api)
#     app.register_blueprint(site_api)
#     app.register_blueprint(metrics_api)
#     app.register_blueprint(packages_api)
#     app.register_blueprint(sites_to_package_api)

#     with app.app_context():
#         db.create_all()

#     app.run()


from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://developer:41b387c1-2cf9-4436-85fa-7c75093b7d14@test-rds-dev.colcjtm9obot.eu-west-1.rds.amazonaws.com:5432/metrics_dev'
db = SQLAlchemy(app)

# Define the models
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text)
    address = db.Column(db.Text)
    phone_number = db.Column(db.Text)
    password=db.Column(db.Integer)

class Package(db.Model):
    __tablename__ = 'packages'
    package_id = db.Column(db.Integer, primary_key=True)
    cost_per_month = db.Column(db.Integer)
    storage_gb = db.Column(db.Float)
    disc_cache = db.Column(db.Float)
    disc_a_gb = db.Column(db.Float)
    disc_b_gb = db.Column(db.Float)
    cpu_percent = db.Column(db.Float)
    cpu_tic = db.Column(db.Float)

class PackageToUser(db.Model):
    __tablename__ = 'packages_to_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    package_id = db.Column(db.Integer, db.ForeignKey('packages.package_id'))

class Site(db.Model):
    __tablename__ = 'sites'
    site_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

class SiteToPackage(db.Model):
    __tablename__ = 'sites_to_package'
    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.package_id'))
    site_id = db.Column(db.Integer, db.ForeignKey('sites.site_id'))

class UsagePerSite(db.Model):
    __tablename__ = 'usage_per_site'
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.site_id'))
    time = db.Column(db.TIMESTAMP(timezone=True))
    storage_gb = db.Column(db.Float)
    disc_cache = db.Column(db.Float)
    disc_a_gb = db.Column(db.Float)
    disc_b_gb = db.Column(db.Float)
    cpu_percent = db.Column(db.Float)
    cpu_tic = db.Column(db.Float)

class Metric(db.Model):
    __tablename__ = 'metrics'
    event_uuid = db.Column(db.Integer, primary_key=True)
    event_time = db.Column(db.TIMESTAMP(timezone=True))
    site_id = db.Column(db.Integer, db.ForeignKey('sites.site_id'))
    storage_gb = db.Column(db.Float)
    disc_cache = db.Column(db.Float)
    disc_a_gb = db.Column(db.Float)
    disc_b_gb = db.Column(db.Float)
    cpu_percent = db.Column(db.Float)
    cpu_tic = db.Column(db.Float)

# API endpoints

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'user_id': user.user_id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'address': user.address,
            'phone_number': user.phone_number
        }
        user_list.append(user_data)
    return jsonify(user_list)

@app.route('/getPackages', methods=['GET'])
def get_packages():
    packages = Package.query.all()
    package_list = []
    for package in packages:
        package_data = {
            'package_id': package.package_id,
            'cost_per_month': package.cost_per_month,
            'storage_gb': package.storage_gb,
            'disc_cache': package.disc_cache,
            'disc_a_gb': package.disc_a_gb,
            'disc_b_gb': package.disc_b_gb,
            'cpu_percent': package.cpu_percent,
            'cpu_tic': package.cpu_tic
        }
        package_list.append(package_data)
    return jsonify(package_list)


@app.route('/packages_to_users', methods=['GET'])
def get_packages_to_users():
    package_to_users = PackageToUser.query.all()
    package_to_user_list = []
    for package_to_user in package_to_users:
        package_to_user_data = {
            'id': package_to_user.id,
            'user_id': package_to_user.user_id,
            'package_id': package_to_user.package_id
        }
        package_to_user_list.append(package_to_user_data)
    return jsonify(package_to_user_list)


@app.route('/sites', methods=['GET'])
def get_sites():
    sites = Site.query.all()
    site_list = []
    for site in sites:
        site_data = {
            'site_id': site.site_id,
            'user_id': site.user_id
        }
        site_list.append(site_data)
    return jsonify(site_list)


@app.route('/sites_to_packages', methods=['GET'])
def get_sites_to_packages():
    sites_to_packages = SiteToPackage.query.all()
    site_to_package_list = []
    for site_to_package in sites_to_packages:
        site_to_package_data = {
            'id': site_to_package.id,
            'package_id': site_to_package.package_id,
            'site_id': site_to_package.site_id
        }
        site_to_package_list.append(site_to_package_data)
    return jsonify(site_to_package_list)


@app.route('/usage_per_site', methods=['GET'])
def get_usage_per_site():
    usage_per_sites = UsagePerSite.query.all()
    usage_per_site_list = []
    for usage_per_site in usage_per_sites:
        usage_per_site_data = {
            'id': usage_per_site.id,
            'site_id': usage_per_site.site_id,
            'time': usage_per_site.time.strftime('%Y-%m-%d %H:%M:%S'),
            'storage_gb': usage_per_site.storage_gb,
            'disc_cache': usage_per_site.disc_cache,
            'disc_a_gb': usage_per_site.disc_a_gb,
            'disc_b_gb': usage_per_site.disc_b_gb,
            'cpu_percent': usage_per_site.cpu_percent,
            'cpu_tic': usage_per_site.cpu_tic
        }
        usage_per_site_list.append(usage_per_site_data)
    return jsonify(usage_per_site_list)


@app.route('/metrics', methods=['GET'])
def get_metrics():
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
    return jsonify(metric_list)




##################################   more functions:





# User Login
@app.route('/login', methods=['POST'])
def login():
    # Retrieve email and password from the request body
    data = request.get_json()
    # email = data.get('email')
    user_id=data.get('user_id')
    password = data.get('password')
    # first_name=data.get('first_name')

    user = User.query.filter_by(user_id=user_id,password=password).first()

    if user:
        # User is authenticated, perform further actions
        # Generate an access token
        
        # access_token = create_access_token(identity=user.user_id)
        
        # Return the access token in the response
        return jsonify({'access_token': 'access_token'})
    else:
        # Invalid email or password
        return jsonify({'message': 'Invalid email or password'})

    
    

# Get User's Packages
@app.route('/<int:user_id>/packages', methods=['GET'])
def get_user_packages(user_id):
    
    # Query the database to retrieve the user's packages
    packages = Package.query\
        .join(PackageToUser, PackageToUser.package_id == Package.package_id)\
        .filter(PackageToUser.user_id == user_id)\
        .all()

    # Prepare the response data
    package_list = []
    for package in packages:
        package_data = {
            'package_id': package.package_id,
            'cost_per_month': package.cost_per_month,
            'storage_gb': package.storage_gb,
            'disc_cache': package.disc_cache,
            'disc_a_gb': package.disc_a_gb,
            'disc_b_gb': package.disc_b_gb,
            'cpu_percent': package.cpu_percent,
            'cpu_tic': package.cpu_tic
        }
        package_list.append(package_data)

    # Return the response
    # return jsonify({'packages': package_list})
    temp=[{'timestamp': '2023-06-11 11:15:32', 'storage_gb': 162.97, 'disc_cache': 44.37, 'disc_a_gb': 456.66, 'disc_b_gb': 276.68, 'cpu_percent': 22.42, 'cpu_tic': 84.38}, {'timestamp': '2023-06-18 11:15:32', 'storage_gb': 141.47, 'disc_cache': 87.73, 'disc_a_gb': 327.57, 'disc_b_gb': 121.29, 'cpu_percent': 46.95, 'cpu_tic': 790.73}, {'timestamp': '2023-06-25 11:15:32', 'storage_gb': 109.29, 'disc_cache': 86.02, 'disc_a_gb': 358.84, 'disc_b_gb': 162.84, 'cpu_percent': 28.95, 'cpu_tic': 171.08}, {'timestamp': '2023-07-02 11:15:32', 'storage_gb': 155.35, 'disc_cache': 23.87, 'disc_a_gb': 307.42, 'disc_b_gb': 383.72, 'cpu_percent': 69.09, 'cpu_tic': 74.92}, {'timestamp': '2023-07-09 11:15:32', 'storage_gb': 189.12, 'disc_cache': 97.8, 'disc_a_gb': 381.77, 'disc_b_gb': 237.74, 'cpu_percent': 91.33, 'cpu_tic': 127.22}]
        
    return jsonify({'packages':temp})

# Get Package Usage for the Last Month
@app.route('/<int:user_id>/packages/<int:package_id>/usage', methods=['GET'])
def get_package_usage(user_id, package_id):
    # Retrieve the start_date and end_date from the query parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Query the database to retrieve the package usage for the specified period
    usage = UsagePerSite.query\
        .join(SiteToPackage, SiteToPackage.site_id == UsagePerSite.site_id)\
        .filter(SiteToPackage.package_id == package_id)\
        .filter(UsagePerSite.time >= start_date, UsagePerSite.time <= end_date)\
        .all()

    # Prepare the response data
    usage_list = []
    for usage_per_site in usage:
        usage_data = {
            'time': usage_per_site.time,
            'storage_gb': usage_per_site.storage_gb,
            'disc_cache': usage_per_site.disc_cache,
            'disc_a_gb': usage_per_site.disc_a_gb,
            'disc_b_gb': usage_per_site.disc_b_gb,
            'cpu_percent': usage_per_site.cpu_percent,
            'cpu_tic': usage_per_site.cpu_tic
        }
        usage_list.append(usage_data)

    # Return the response
    return jsonify({'usage': usage_list})

@app.route('/packages/<int:package_id>')
def get_package(package_id):
    package=Package.query.filter_by(package_id=package_id).first()
    if package:
        return jsonify({"package":package})
    else:
        return jsonify({'message':'No such package.'})

# Get Sites Included in a Package
@app.route('/<int:package_id>/sites', methods=['GET'])
def get_package_sites(package_id):
    # Query the database to retrieve the sites included in the package
    sites = Site.query\
        .join(SiteToPackage, SiteToPackage.site_id == Site.site_id)\
        .filter(SiteToPackage.package_id == package_id)\
        .all()

    # Prepare the response data
    site_list = []
    for site in sites:
        site_data = {
            'site_id': site.site_id,
            'user_id': site.user_id
        }
        site_list.append(site_data)

    # Return the response
    return jsonify({'sites': site_list})


# Get Usage for a Specific Site
@app.route('/<int:site_id>/usage', methods=['GET'])
def get_site_usage(site_id):
    # Retrieve the start_date and end_date from the query parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Query the database to retrieve the usage for the specified site and period
    usage = UsagePerSite.query\
        .filter(UsagePerSite.site_id == site_id)\
         .filter(UsagePerSite.time >= start_date, UsagePerSite.time <= end_date)\
            .all()

    # Prepare the response data
    usage_list = []
    for usage_per_site in usage:
        usage_data = {
            'time': usage_per_site.time,
            'storage_gb': usage_per_site.storage_gb,
            'disc_cache': usage_per_site.disc_cache,
            'disc_a_gb': usage_per_site.disc_a_gb,
            'disc_b_gb': usage_per_site.disc_b_gb,
            'cpu_percent': usage_per_site.cpu_percent,
            'cpu_tic': usage_per_site.cpu_tic
        }
        usage_list.append(usage_data)

    # Return the response
    return jsonify({'usage': usage_list})



# Get Sites Included in a Package
# @app.route('/<int:package_id>/sites', methods=['GET'])
# def get_package_sites(package_id):
#     # Query the database to retrieve the sites included in the package
#     sites = Site.query\
#         .join(SiteToPackage, SiteToPackage.site_id == Site.site_id)\
#         .filter(SiteToPackage.package_id == package_id)\
#         .all()

#     # Prepare the response data
#     site_list = []
#     for site in sites:
#         site_data = {
#             'site_id': site.site_id,
#             'user_id': site.user_id
#         }
#         site_list.append(site_data)

#     # Return the response
#     return jsonify({'sites': site_list})

# Get Usage for a Specific Site
# @app.route('/api/<int:site_id>/usage', methods=['GET'])
# def get_site_usage(site_id):
#     # Retrieve the start_date and end_date from the query parameters
#     start_date = request.args.get('start_date')
#     end_date = request.args.get('end_date')

#     # Query the database to retrieve the usage for the specified site and period
#     usage = UsagePerSite.query\
#         .filter(UsagePerSite.site_id == site_id)\
#         .filter(UsagePerSite.time >= start_date, UsagePerSite.time <= end_date)\
#         .all()

#     # Prepare the response data
#     usage_list = []
#     for usage_per_site in usage:
#         usage_data = {
#             'time': usage_per_site.time,
#             'storage_gb': usage_per_site.storage_gb,
#             'disc_cache': usage_per_site.disc_cache,
#             'disc_a_gb': usage_per_site.disc_a_gb,
#             'disc_b_gb': usage_per_site.disc_b_gb,
#             'cpu_percent': usage_per_site.cpu_percent,
#             'cpu_tic': usage_per_site.cpu_tic
#         }
#         usage_list.append(usage_data)

#     # Return the response
#     return jsonify({'usage': usage_list})


if __name__ == '__main__':
    app.run()

