from src.app import db
from flask_login import UserMixin
from sqlalchemy import Sequence


class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, Sequence(name='user_id_seq'))
    email = db.Column(db.String(100), primary_key=True)
    full_name = db.Column(db.String(100), index=True)
    avatar_url = db.Column(db.String(100), index=True)
    password_hash = db.Column(db.String(100), index=True)

    # overriding the get_id to return email - that we used at the primary key
    def get_id(self):
        return self.email

    def __repr__(self):
        return f"<User: full name: {self.full_name}, email: {self.email}>"


def ensure():
    db.create_all()
