from flask import request, jsonify
from app import db, limiter
from app.models.user import User
from . import user_api

@user_api.route('/register', methods=['POST'])
@limiter.limit("5 per minute")  # Limiting registration route
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@user_api.route('/login', methods=['POST'])
@limiter.limit("10 per minute")  # Limiting login route
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
