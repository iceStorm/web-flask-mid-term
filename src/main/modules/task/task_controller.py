import sys

from flask import Blueprint, render_template, redirect
from flask.globals import current_app, request
from flask.helpers import flash, url_for
from flask_login import login_required, current_user

task = Blueprint('task', __name__, template_folder='templates')
from src.main.modules.task.forms.add_task_form import AddTaskForm
from src.main.modules.task.decorators.task_owner import task_owner
from src.main.modules.task.task_service import TaskService


@task.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddTaskForm()

    if request.method == 'GET':
        return render_template('add-new.html', form=form)

    # validate the form
    if not form.validate_on_submit():
        flash('Form error!', category='error')

        # re-assigning the email (id) to the form
        return render_template('add-new.html', form=form)

    # all done. let's handle the main process
    form.user_id.data = current_user.email  # assigning the user's email (as id)

    try:
        TaskService.add_new_task(form=form)
        flash(f"\"{form.name.data}\" added!", category='success')
        return redirect('/')
    except NameError as err:
        flash('Error occurred when adding the Task', category='error')
        print('error', err)
        return render_template('add-new.html', form=form)


@task.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
@task_owner
def edit(the_task):
    form = AddTaskForm()

    # on get request -- showing the form view
    if request.method == 'GET':
        form.name.data = the_task.name
        form.description.data = the_task.description
        form.priority_id.data = the_task.priority_id
        return render_template('add-new.html', isEditing=True, form=form)


    # on post request --- updating the data
    if not form.validate_on_submit():
        flash('Form error!', category='error')
        return render_template('add-new.html', isEditing=True, form=form)

    try:
        TaskService.update_task(the_task.task_id, form)
        flash('Updated!', category='success')
        return redirect('/')
    except Exception as e:
        print('\n\n\nerror', sys.exc_info[0])
        flash('Error when saving changes!', category='error')
        return render_template('add-new.html', isEditing=True, form=form)


@task.route('/duplicate/<int:task_id>', methods=['GET'])
@login_required
@task_owner
def duplicate(the_task):
    try:
        TaskService.duplicate_task(the_task)

        flash(f'Duplicated the "{the_task.name}"', category='success')
        return redirect('/')
    except:
        print('\n\n\nerror', sys.exc_info[0])
        flash('Error occurred when duplicating this task!', category='error')
        return redirect('/')


@task.route('/trash/<int:task_id>', methods=['GET'])
@login_required
@task_owner
def trash(the_task):
    try:
        # from src.main.modules.task.task_service import TaskService
        TaskService.move_to_trash(the_task)

        flash(f'Moved "{the_task.name}" to the Trash!', category='success')
        return redirect('/')
    except:
        print('\n\n\nerror', sys.exc_info[0])
        flash('Error occurred when moving this task to the Trash!', category='error')
        return redirect('/')


@task.route('/restore/<int:task_id>', methods=['GET'])
@login_required
@task_owner
def restore(the_task):
    try:
        # from src.main.modules.task.task_service import TaskService
        TaskService.restore_from_trash(the_task)

        flash(f'Restored "{the_task.name}"!', category='success')
        return redirect('/')
    except:
        print('\n\n\nerror', sys.exc_info[0])
        flash('Error occurred when restoring this task!', category='error')
        return redirect('/')


@task.route('/delete/<int:task_id>', methods=['GET'])
@login_required
@task_owner
def delete(the_task):
    try:
        # from src.main.modules.task.task_service import TaskService
        TaskService.remove_task(the_task)

        flash(f'Permanently deleted the "{the_task.name}"', category='success')
        return redirect(url_for('task.trash_can'))
    except:
        print('\n\n\nerror', sys.exc_info[0])
        flash('Error occurred when deleting this task!', category='error')
        return redirect('/')


@task.route('/mark_done/<int:task_id>', methods=['GET'])
@login_required
@task_owner
def mark_done(the_task):
    try:
        # from src.main.modules.task.task_service import TaskService
        TaskService.mark_as_done(the_task)

        flash(f'Marked done for "{the_task.name}"', category='success')
        return redirect(url_for('index.index'))
    except:
        print('\n\n\nerror', sys.exc_info[0])
        flash('Error occurred when marking done this task!', category='error')
        return redirect('/')


@task.route('/mark_undone/<int:task_id>', methods=['GET'])
@login_required
@task_owner
def mark_undone(the_task):
    try:
        # from src.main.modules.task.task_service import TaskService
        TaskService.mark_as_undone(the_task)

        flash(f'Reverted "{the_task.name}"', category='success')
        return redirect(url_for('index.index'))
    except:
        print('\n\n\nerror', sys.exc_info[0])
        flash('Error occurred when marking done this task!', category='error')
        return redirect('/')



@task.route('/trash', methods=['GET'])
@login_required
def trash_can():
    per_page = request.args.get('per_page')
    page_index = request.args.get('page_index')

    # from src.main.modules.task.task_service import TaskService
    trashed_tasks = TaskService.get_tasks_by(
        user_id=current_user.email,
        trashed=True,
        done=False,
        per_page=int(per_page or 5),
        page_index=int(page_index or 1)
    )

    return render_template('trash-can.html', trashed_tasks=trashed_tasks)
