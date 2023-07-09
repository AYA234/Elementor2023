from flask import Blueprint, jsonify, request
from dal.user_dal import get_all_users
from models.users_model import User

user_api = Blueprint('user_api', __name__)

@user_api.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users)

@user_api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    user = User.query.filter_by(email=email, password=password).first()
    # if user:
    #     access_token = create_access_token(identity=user.user_id)
    #     return jsonify({'access_token': access_token})
    # else:
    #     return jsonify({'message': 'Invalid email or password'})
