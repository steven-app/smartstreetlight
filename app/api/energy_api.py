from flask import request, jsonify
from app import db
from app.models.energy import Energy
from . import energy_api

@energy_api.route('/energy', methods=['GET'])
def get_energy_data():
    energy_data = Energy.query.all()
    return jsonify([data.consumption for data in energy_data])

@energy_api.route('/energy', methods=['POST'])
def add_energy_data():
    data = request.get_json()
    consumption = data.get('consumption')
    timestamp = data.get('timestamp')

    energy = Energy(consumption=consumption, timestamp=timestamp)
    db.session.add(energy)
    db.session.commit()

    return jsonify({"message": "Energy data added"}), 201
