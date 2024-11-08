from app import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255))
    level = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Log {self.message}>'
