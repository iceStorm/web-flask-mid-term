from src.run import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}

    email = db.Column(db.String(100), primary_key=True)
    full_name = db.Column(db.String(100))
    avatar_url = db.Column(db.String(100))
    password_hash = db.Column(db.String(100))

    # overriding the get_id to return email - that we used at the primary key
    def get_id(self):
        return self.email


def ensure():
    db.create_all()
