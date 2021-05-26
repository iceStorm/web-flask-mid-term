from src.main.modules.user.user_model import User
from werkzeug.security import check_password_hash
from src.run import db


class AuthService:
    @staticmethod
    def send_reset_password_email(email: str) -> None:
        raise Exception("The email is not exists on the system")

    @staticmethod
    def is_user_already_exists(email):
        return User.query.get(email) is not None

    @staticmethod
    def check_password(user: User, raw_password: str) -> bool:
        return check_password_hash(user.password_hash, raw_password)

    @staticmethod
    def register(new_user: User):
        db.session.add(new_user)
        db.session.commit()
        pass
