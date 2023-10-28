from flask import Blueprint, request, jsonify, make_response
from flask_login import login_required, current_user, logout_user, login_user
from app import db, login_manager, socketio
from app.models import User, Guest
from werkzeug.security import generate_password_hash, check_password_hash

api_bp = Blueprint('api', __name__)

connected_users = []

def configure_api_routes(app, db, login_manager, socketio):
    @socketio.on('connect')
    def connect():
        print('Connected')

        sid = request.sid

        connected_users.append(sid)

        guest = Guest(sid=sid, username = 'Guest' + str(len(connected_users)))
                               
        db.session.add(guest)
        db.session.commit()

        print(connected_users)

    @socketio.on('disconnect')
    def disconnect():
        print('Disconnected')

        guest = Guest.query.filter_by(sid=request.sid).first()
        db.session.delete(guest)
        db.session.commit()

        connected_users.remove(request.sid)
        print(connected_users)

    @api_bp.route('/auth/check_username', methods=['GET', 'POST'])
    def check_username():
        name = request.form.get('username')

        if User.query.filter_by(username=name).first():
            return jsonify({'message': 'Username already exists.'}), 400 

        return jsonify({'message': 'Username is available.'}), 200

    @api_bp.route('/auth/add_guest', methods=['GET', 'POST'])
    def add_guest():
        name = request.form.get('username')

        if Guest.query.filter_by(username=name).first() or User.query.filter_by(username=name).first():
            return jsonify({'message': 'Username already exists.'}), 400

        guest = Guest(username=name)
        db.session.add(guest)
        db.session.commit()

        return jsonify({'message': 'Guest added.'}), 200

    @api_bp.route('/auth/delete_guest', methods=['GET', 'POST'])
    def delete_guest():
        pass

    @api_bp.route('/auth/check_email', methods=['GET', 'POST'])
    def check_email():
        email = request.form.get('email')

        if User.query.filter_by(email=email).first():
            return jsonify({'message': 'Email already exists.'}), 400 

        return jsonify({'message': 'Email is available.'}), 200

    @api_bp.route('/auth/create_lobby', methods=['GET', 'POST'])
    def create_lobby():
        pass

    @api_bp.route('/auth/join_lobby', methods=['GET', 'POST'])
    def join_lobby():
        pass