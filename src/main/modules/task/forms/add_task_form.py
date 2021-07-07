from flask_wtf import FlaskForm
from wtforms.fields import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired, Length, Optional

from src.main.modules.priority.fields.priority_field import PriorityField
from src.main.modules.project.fields.deadline_field import DeadlineField


class AddTaskForm(FlaskForm):
    # def __init__(self):
    #     super(AddNewTaskForm, self).__init__()
    #     self.priority_id.choices = [(p.id, p.name) for p in Priority.query]

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


    # custom field
    priority_id = PriorityField()


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

