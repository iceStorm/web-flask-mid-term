from src.run import db


class User(db.Model):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}

    email = db.Column(db.String(100), primary_key=True)
    full_name = db.Column(db.String(100))
    password_hash = db.Column(db.String(100))


def ensure():
    db.create_all()
