from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

from src.main.modules.project.fields.deadline_field import DeadlineField


class AddProjectForm(FlaskForm):
    name = StringField(
        label='Enter project name',
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

    descriptions = StringField(
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

    # custom field
    deadline = DeadlineField()

