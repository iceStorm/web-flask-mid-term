import os

from flask import current_app
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

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


    @staticmethod
    def update(email: str, user: User):
        the_user = User.query.get(email)
        the_user.full_name = user.full_name

        # checking if the avatar is modified
        print('avatar_path:', user.avatar_url)

        if user.avatar_url == 'null':
            print('resetting the avatar_url...')
            the_user.avatar_url = None  # removing the avatar_url value
        elif user.avatar_url is not None:
            the_user.avatar_url = user.avatar_url

        db.session.commit()


    @staticmethod
    def save_avatar_image(form_image_data: FileStorage) -> str:
        the_path = ''

        if form_image_data:
            the_avatar_name = secure_filename(filename=form_image_data.filename)

            # saving the avatar image
            # print('current_app.instance_path:', current_app.instance_path)
            the_path = os.path.abspath(os.path.join(current_app.instance_path, 'main/base/static/users/avatars', the_avatar_name))
            form_image_data.save(the_path)

        # returning the saved image path
        return the_path
