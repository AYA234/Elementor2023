from models.users_model import User

def get_all_users():
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
    return user_list


