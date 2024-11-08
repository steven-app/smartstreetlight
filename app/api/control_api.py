from flask import request, jsonify
from . import control_api

@control_api.route('/control', methods=['POST'])
def control_device():
    data = request.get_json()
    device_id = data.get('device_id')
    action = data.get('action')

    # Add logic to control the device based on action and device_id
    return jsonify({"message": f"Device {device_id} action {action} executed"}), 200
