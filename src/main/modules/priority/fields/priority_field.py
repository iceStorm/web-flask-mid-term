from wtforms.fields import SelectField
from wtforms.validators import DataRequired, Length


class PriorityField(SelectField):

    # **kwargs is always required
    def __init__(self, **kwargs):
        super(PriorityField, self).__init__(**kwargs)

        # custom logics below
        # filling the choices for this SelectField
        from src.main.modules.priority.priority_model import Priority
        self.choices = [(p.id, p.name) for p in Priority.query]


        # data type
        self.coerce = int

        # html label tag
        self.label.text = 'Priority'

        # for displaying icon
        self.description = {
            'icon': {
                'origin': 'icons/outline/alert-outline.svg',
            }
        }

        # validators
        self.validators=[
            DataRequired(message='Please assign a Priority'),
        ]
