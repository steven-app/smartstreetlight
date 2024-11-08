from app import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120))
    ip_address = db.Column(db.String(45))
    status = db.Column(db.String(20), default="active")

    def __repr__(self):
        return f'<Device {self.name}>'
