from datetime import datetime

from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired


class DeadlineField(DateTimeLocalField):

    # **kwargs is always required
    def __init__(self, **kwargs):
        super(DeadlineField, self).__init__(**kwargs)


        # format
        self.format = format='%Y-%m-%dT%H:%M'

        # html label tag
        self.label.text = 'Deadline'

        # for displaying icon
        self.description = {
            'icon': {
                'origin': 'icons/outline/alarm-outline.svg',
            }
        }

        # validators
        self.validators=[
            DataRequired(message='Please specify a Deadline date/time'),
        ]

    # run this validation after the normal validations have passed
    def post_validate(self, form, validation_stopped):
        if validation_stopped:
            return False

        if self.data < datetime.now():
            self.errors.append('The deadline cannot smaller than today!')
            return False

        return True
