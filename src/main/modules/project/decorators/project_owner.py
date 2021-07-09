import inspect
from functools import wraps
from flask import g, request, redirect, url_for, flash
from flask_login import current_user
from src.main.modules.project.project_model import Project


def project_owner(f):
    """
    Decorator that will read the query parameters for the request.
    The names are the names that are mapped in the function.
    """
    @wraps(f)
    def logic(*args, **kwargs):
        params = dict(kwargs)
        project_id = params['project_id']

        if project_id:
            the_project = Project.query.get(project_id)

            if the_project:
                if the_project.user_id == current_user.email:
                    # "the_project" wil be passed as a callback param to the
                    # actual function that implements this decorator"
                    return f(the_project)

                flash('You don\'t own this Project!', category='warning')
                return redirect(url_for('index.index'))

            flash('The project no longer exists!', category='error')
            return redirect(url_for('index.index'))

        return f(*args, **kwargs)

    return logic
