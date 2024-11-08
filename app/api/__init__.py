from flask import Blueprint

# Initialize API blueprints for each module
user_api = Blueprint('user_api', __name__)
role_api = Blueprint('role_api', __name__)
device_api = Blueprint('device_api', __name__)
alert_api = Blueprint('alert_api', __name__)
energy_api = Blueprint('energy_api', __name__)
control_api = Blueprint('control_api', __name__)
map_api = Blueprint('map_api', __name__)
meter_api = Blueprint('meter_api', __name__)
strategy_api = Blueprint('strategy_api', __name__)
db_config_api = Blueprint('db_config_api', __name__)
