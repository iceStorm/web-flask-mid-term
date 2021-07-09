from flask_wtf import FlaskForm
from wtforms.fields import StringField, HiddenField, SelectField
from wtforms.validators import DataRequired, Length, Optional

from src.main.modules.priority.fields.priority_field import PriorityField
from src.main.modules.project.fields.deadline_field import DeadlineField
from src.main.modules.project.fields.projects_field import ProjectsField
from src.main.modules.status.fields.status_field import StatusField


class AddTaskForm(FlaskForm):

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
    priority_id = PriorityField()

    # custom field
    status_id = StatusField()

    # custom field
    deadline = DeadlineField()

    # custom field
    project_id = ProjectsField()

    # custom validating
    def validate(self):
        if not FlaskForm.validate(self):
            return False

        from src.main.modules.project.project_model import Project
        the_project = Project.query.get(self.project_id.data)

        if self.deadline.data > the_project.deadline:
            self.deadline.errors.append(f'The deadline cannot greater than its parent project [{the_project.deadline}]')
            return False

        return True
