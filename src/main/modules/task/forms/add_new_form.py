from flask_wtf import FlaskForm
from wtforms.fields import StringField, HiddenField
from wtforms.fields.core import SelectField
from wtforms.validators import DataRequired, Length, Optional


class AddNewTaskForm(FlaskForm):
    name = StringField(
        label='Enter task name',
        description={
            'icon': {
                'origin': 'icons/outline/at-outline.svg',
            },
        },
        validators=[
            DataRequired(message='Please fill out this field'),
            Length(max=50, min=5, message='The name must between 5 & 50 characters.'),
        ],
    )

    description = StringField(
        label='Enter description',
        description={
            'icon': {
                'origin': 'icons/outline/chatbox-outline.svg',
            },
        },
        validators=[
            DataRequired(message='Please fill out this field'),
            Length(max=255, min=5, message='The name must between 5 & 255 characters.'),
        ],
    )

    priority_id = SelectField(
        label='Priority',
        coerce=int,
        description={
            'icon': {
                'origin': 'icons/outline/alert-outline.svg',
            },
        },
        validators=[
            DataRequired(message='Please choose a priority.'),
        ],
    )

    user_id = HiddenField(
        label='User id',
        description={
            'icon': {
                'origin': 'icons/outline/finger-print-outline.svg',
            },
        },
        validators=[
            # this field's data will be manually set when needed,
            # regardless (ignoring) any tricks to set wrong data on the client side.
            Optional()
        ],
    )
