from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired


class DeadlineField(DateTimeLocalField):

    # **kwargs is always required
    def __init__(self, **kwargs):
        super(DeadlineField, self).__init__(**kwargs)


        # data type
        self.coerce = int

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
