from app import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    permissions = db.Column(db.String(120))  # Permissions stored as a comma-separated string

    def __repr__(self):
        return f'<Role {self.name}>'
