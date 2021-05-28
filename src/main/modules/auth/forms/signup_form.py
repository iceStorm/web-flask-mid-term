from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo, Regexp, ValidationError
import re


def check_password_format(form, field):
    if len(field.data) < 6 or len(field.data) > 50:
        raise ValidationError(message='The password must between 6 and 50 characters')
    else:
        password_regex_pattern = '[a-zA-Z0-9]'
        if not re.match(password_regex_pattern, field.data):
            raise ValidationError(message='The password can only contains numbers, letters')


def is_email_exists(form, field):
    from src.main.modules.user.user_model import User
    if User.query.get(field.data) is not None:
        raise ValidationError(message='The email is already registered')


class SignUpForm(FlaskForm):
    email = EmailField(
        label='Email',
        render_kw={'autocomplete': 'email'},
        validators=[
            InputRequired(),
            Regexp(regex='^[a-z][a-z0-9_\.]{5,32}@[a-z0-9]{2,}(\.[a-z0-9]{2,4}){1,2}$', message='The email format is invalid'),
            is_email_exists,
        ]
    )

    full_name = StringField(
        label='Full name',
        render_kw={'autocomplete': 'name'},
        validators=[
            InputRequired(message='Please fill out this field'),
            Length(min=2, max=50, message='The length must between 2 and 50 letters'),
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

    re_password = PasswordField(
        label='Re-enter password',
        render_kw={'autocomplete': 'new-password'},
        validators=[
            InputRequired(message='Please fill out this field'),
            check_password_format,
            EqualTo(fieldname='password', message='Password fields does not match'),
        ]
    )
