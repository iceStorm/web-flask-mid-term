from src.app import db
from flask_login import UserMixin
from sqlalchemy import Sequence

from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    __table_args__ = {'extend_existing': True}

    email = db.Column(db.String(100), primary_key=True, index=True)
    full_name = db.Column(db.String(100), index=True, nullable=False)
    avatar_url = db.Column(db.String(100))
    password_hash = db.Column(db.String(255), nullable=False)

    def __init__(self, email=None, full_name=None, raw_password=None, avatar_url=None):
        """
        Creating a new User instance.
        raw_password: this field will be encrypted automatically.
        """
        self.email = email
        self.full_name = full_name
        self.avatar_url = avatar_url

        password_hash = User.gen_password_hash(raw_password)
        print(f'hashing the password {raw_password}:', password_hash)
        self.password_hash = password_hash

    @staticmethod
    def gen_password_hash(raw_password):
        return generate_password_hash(raw_password, method='sha256') if raw_password else None

    def get_id(self):
        """
        Overriding the get_id to return email - that we used at the primary key
        """
        return self.email

    def __repr__(self):
        return f"<User: full name: {self.full_name}, email: {self.email}>"

    def check_password(self, raw_password: str):
        """
        Checking if the raw_password matches with the password of this User instance.
        """
        print('checking the password:', raw_password)
        return check_password_hash(self.password_hash, raw_password)

