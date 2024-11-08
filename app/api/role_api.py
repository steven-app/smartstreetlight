from flask import request, jsonify
from app import db
from app.models.role import Role
from . import role_api

@role_api.route('/roles', methods=['GET'])
def get_roles():
    roles = Role.query.all()
    return jsonify([role.name for role in roles])

@role_api.route('/roles', methods=['POST'])
def create_role():
    data = request.get_json()
    name = data.get('name')
    permissions = data.get('permissions', "")

    role = Role(name=name, permissions=permissions)
    db.session.add(role)
    db.session.commit()

    return jsonify({"message": "Role created"}), 201
