import inspect
from functools import wraps
from flask import g, request, redirect, url_for, flash
from flask_login import current_user
from src.main.modules.task.task_model import Task


def task_owner(f):
    """
    Decorator that will read the query parameters for the request.
    The names are the names that are mapped in the function.
    """
    @wraps(f)
    def logic(*args, **kwargs):
        params = dict(kwargs)
        task_id = params['task_id']

        if task_id:
            the_task = Task.query.get(task_id)

            if the_task:
                if the_task.user_id == current_user.email:
                    # "the_task" wil be passed as a callback param to the
                    # actual function that implements this decorator"
                    return f(the_task)

                flash('You don\'t own this Task!', category='warning')
                return redirect(url_for('index.index'))

            flash('The task no longer exists!', category='error')
            return redirect(url_for('index.index'))

        return f(*args, **kwargs)

    return logic
