from flask_login import current_user

from src.app import db


class ProjectService:

    @staticmethod
    def add_new_project(form):
        from src.main.modules.project.project_model import Project

        new_project = Project(
            name=form.name.data,
            descriptions=form.descriptions.data,

            deadline=form.deadline.data,
            status_id=4,
            user_id=current_user.email,
        )

        db.session.add(new_project)
        db.session.commit()


    @staticmethod
    def update_project(form, the_project):

        the_project.name = form.name.data
        the_project.descriptions = form.descriptions.data
        the_project.deadline = form.deadline.data

        db.session.commit()


    @staticmethod
    def delete_project(the_project):

        # firstly, delete its children tasks
        for task in the_project.tasks:
            db.session.delete(task)

        db.session.delete(the_project)
        db.session.commit()