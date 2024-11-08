from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .config import Config

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    limiter.init_app(app)
    
    Session(app)

    from .api import user_api, role_api, device_api, alert_api, energy_api, control_api, map_api, meter_api, strategy_api, db_config_api
    app.register_blueprint(user_api)
    app.register_blueprint(role_api)
    app.register_blueprint(device_api)
    app.register_blueprint(alert_api)
    app.register_blueprint(energy_api)
    app.register_blueprint(control_api)
    app.register_blueprint(map_api)
    app.register_blueprint(meter_api)
    app.register_blueprint(strategy_api)
    app.register_blueprint(db_config_api)

    return app
