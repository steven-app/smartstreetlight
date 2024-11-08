from app import db

class Energy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consumption = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Energy {self.consumption} kWh>'
