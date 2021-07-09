import sys

from flask import Blueprint, render_template, redirect
from flask.globals import request
from flask.helpers import flash, url_for
from flask_login import login_required, current_user

task = Blueprint('task', __name__, template_folder='templates')
from src.main.modules.task.decorators.task_owner import task_owner
from src.main.modules.task.forms.add_task_form import AddTaskForm
from src.main.modules.task.task_service import TaskService


@task.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddTaskForm()

    # validate the form
    if not form.validate_on_submit():
        if request.method == 'POST':
            print('error form...')
            flash('Form error!', category='error')

        # re-assigning the email (id) to the form
        form.status_id.data = 4
        form.status_id.render_kw = { 'readonly': 'true', 'style': 'pointer-events: none;' }
        return render_template('add-task.html', form=form)

    try:
        TaskService.add_new_task(form=form)
        flash(f"\"{form.descriptions.data}\" added!", category='success')
        return redirect('/')
    except NameError as err:
        flash('Error occurred when adding the Task', category='error')
        print('error', err)
        return render_template('add-task.html', form=form)


@task.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
@task_owner
def edit(the_task):
    form = AddTaskForm()

    if not form.validate_on_submit():
        if request.method == 'POST':
            flash('Form error!', category='error')

        form.descriptions.data = the_task.descriptions
        form.deadline.data = the_task.deadline

        form.priority_id.data = the_task.priority_id
        form.status_id.data = the_task.status_id
        form.project_id.data = the_task.project_id
        return render_template('add-task.html', isEditing=True, form=form)

    try:
        TaskService.update_task(the_task, form)
        flash('Updated!', category='success')
        return redirect('/')
    except Exception as e:
        print('\n\n\nerror', sys.exc_info[0])
        flash('Error when saving changes!', category='error')
        return render_template('add-task.html', isEditing=True, form=form)


@task.route('/delete/<int:task_id>', methods=['GET'])
@login_required
@task_owner
def delete(the_task):
    try:
        # from src.main.modules.task.task_service import TaskService
        TaskService.remove_task(the_task)

        flash(f'Permanently deleted the "{the_task.descriptions}"', category='success')
        return redirect('/')
    except:
        print('\n\n\nerror', sys.exc_info[0])
        flash('Error occurred when deleting this task!', category='error')
        return redirect('/')

