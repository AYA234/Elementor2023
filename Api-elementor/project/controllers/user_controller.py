from flask import Blueprint, jsonify, request
from dal import users_dal


users_controller = Blueprint('users_controller', __name__)

@users_controller.route('/getAllUsers', methods=['GET'])
def get_users():
    users = users_dal.get_all_users()
    return jsonify(users)

@users_controller.route('/getUserByEmailAndPassword', methods=['POST'])
def get_user_by_email_and_password():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    return jsonify(users_dal.get_user_by_email_and_password(email,password))
    