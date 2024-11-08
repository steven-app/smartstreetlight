from flask import request, jsonify
from app import db
from app.models.device import Device
from . import device_api

@device_api.route('/devices', methods=['GET'])
def get_devices():
    devices = Device.query.all()
    return jsonify([device.name for device in devices])

@device_api.route('/devices', methods=['POST'])
def add_device():
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    ip_address = data.get('ip_address')

    device = Device(name=name, location=location, ip_address=ip_address)
    db.session.add(device)
    db.session.commit()

    return jsonify({"message": "Device added"}), 201
