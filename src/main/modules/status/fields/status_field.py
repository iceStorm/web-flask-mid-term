from wtforms.fields import SelectField
from wtforms.validators import DataRequired


class StatusField(SelectField):

    # **kwargs is always required
    def __init__(self, **kwargs):
        super(StatusField, self).__init__(**kwargs)

        # custom logics here
        self.coerce = int

        # assigning default status
        self.data = 4

        # filling the choices for this SelectField
        from src.main.modules.status.status_model import Status
        self.choices = [(s.id, s.name) for s in Status.query]

        self.label.text = 'Status'

        self.description = {
            'icon': {
                'origin': 'icons/outline/checkbox-outline.svg',
            }
        }

        self.validators=[
            DataRequired(message='Please assign a Status'),
        ]

