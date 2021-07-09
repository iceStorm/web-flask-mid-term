import datetime

from flask_login import current_user
from wtforms import SelectField
from wtforms.validators import DataRequired


class ProjectsField(SelectField):

    # **kwargs is always required
    def __init__(self, **kwargs):
        super(ProjectsField, self).__init__(**kwargs)


        # data type
        self.coerce = int

        # html label tag
        self.label.text = 'Project'

        # filling the choices for this SelectField
        # getting projects belog to this user (logged in user)
        from src.main.modules.project.project_model import Project
        self.choices = [(prj.id, prj.name) for prj in Project.query.filter_by(user_id=current_user.email)]

        # for displaying icon
        self.description = {
            'icon': {
                'origin': 'icons/outline/cube-outline.svg',
            }
        }

        # validators
        self.validators=[
            DataRequired(message='Please assign a project for this Task'),
        ]
