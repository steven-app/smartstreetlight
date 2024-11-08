from flask import request, jsonify
from app import db
from app.models.alert import Alert
from . import alert_api

@alert_api.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = Alert.query.all()
    return jsonify([alert.message for alert in alerts])

@alert_api.route('/alerts', methods=['POST'])
def create_alert():
    data = request.get_json()
    message = data.get('message')
    level = data.get('level')
    timestamp = data.get('timestamp')

    alert = Alert(message=message, level=level, timestamp=timestamp)
    db.session.add(alert)
    db.session.commit()

    return jsonify({"message": "Alert created"}), 201
