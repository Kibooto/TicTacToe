from flask import Blueprint, request, jsonify, make_response
from flask_login import login_required, current_user, logout_user, login_user
from app import db, login_manager
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

api_bp = Blueprint('api', __name__)

@api_bp.route('/auth/check_username', methods=['GET', 'POST'])
def check_username():
    name = request.form.get('username')
    
    if User.query.filter_by(username=name).first():
        return jsonify({'message': 'Username already exists.'}), 400 

    return jsonify({'message': 'Username is available.'}), 200

@api_bp.route('/auth/check_email', methods=['GET', 'POST'])
def check_email():
    email = request.form.get('email')
    
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists.'}), 400 

    return jsonify({'message': 'Email is available.'}), 200
