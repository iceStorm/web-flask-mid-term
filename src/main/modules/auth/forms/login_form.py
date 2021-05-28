from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo, Regexp, ValidationError

import re
from src.main.modules.user.user_model import User
from src.main.modules.auth.auth_service import AuthService


def check_password_format(form, field):
    if len(field.data) < 6 or len(field.data) > 50:
        raise ValidationError(message='The password must between 6 and 50 characters')
    else:
        password_regex_pattern = '[a-zA-Z0-9]'
        if not re.match(password_regex_pattern, field.data):
            raise ValidationError(message='The password can only contains numbers, letters')


def is_email_exists(form, field):
    """
    Checking if the email that client entered is have already exist.
    """
    if not AuthService.is_user_already_exists(field.data):
        raise ValidationError(message='The email is not registered yet')


class LoginForm(FlaskForm):
    email = EmailField(
        label='Email',
        render_kw={'autocomplete': 'email'},
        validators=[
            InputRequired(),
            Regexp(regex='', message='The email format is invalid'),
            is_email_exists,
        ]
    )

    password = PasswordField(
        label='Password',
        render_kw={'autocomplete': 'new-password'},
        validators=[
            InputRequired(message='Please fill out this field'),
            check_password_format,
        ]
    )

    remember = BooleanField(
        label='Remember',
    )

    # overriding the validate function
    def validate(self):
        # first, validate the above requirements by passing this instance to the FlaskForm.validate()
        if not FlaskForm.validate(self):
            return False

        # checking if the provided password is not True (with the one in the database)
        # the user instance below is always exists because the form's email validation did check.
        user = User.query.get(self.email.data)
        if user.check_password(self.password.data):
            self.password.errors.append('The password you just provided was wrong')
            return False

        return True

