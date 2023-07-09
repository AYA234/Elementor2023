from app import db
from models.packages_to_users_model import PackageToUser

def get_all_packages_to_users():
    package_to_users = PackageToUser.query.all()
    package_to_user_list = []
    for package_to_user in package_to_users:
        package_to_user_data = {
            'id': package_to_user.id,
            'user_id': package_to_user.user_id,
            'package_id': package_to_user.package_id
        }
        package_to_user_list.append(package_to_user_data)
    return package_to_user_list
