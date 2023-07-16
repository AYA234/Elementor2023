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
            'phone_number': user.phone_number,
            'password':user.password
        }
        user_list.append(user_data)
    return user_list

def get_user_by_email_and_password(email,password):    
    user = User.query.filter_by(email=email, password=password).first()
    if user:     
        user_data = {
            'user_id': user.user_id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'address': user.address,
            'phone_number': user.phone_number,
            'password':user.password
        }
        # access_token = create_access_token(identity=user.user_id)
        return user_data
          
    else:
        return {'message': 'Invalid email or password'}

