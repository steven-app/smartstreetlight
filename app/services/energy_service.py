from app.models.energy import Energy
from app import db

class EnergyService:
    @staticmethod
    def log_consumption(consumption, timestamp):
        energy = Energy(consumption=consumption, timestamp=timestamp)
        db.session.add(energy)
        db.session.commit()

    @staticmethod
    def get_consumption_summary():
        return Energy.query.all()
