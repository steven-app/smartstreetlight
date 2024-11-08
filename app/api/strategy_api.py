from flask import request, jsonify
from . import strategy_api

@strategy_api.route('/strategy', methods=['POST'])
def manage_strategy():
    data = request.get_json()
    strategy_id = data.get('strategy_id')

    # Add logic to manage strategy
    return jsonify({"message": f"Strategy {strategy_id} managed successfully"}), 200
