from flask import Blueprint, render_template, request
from flask.helpers import flash
from flask_login import login_required
from werkzeug.utils import redirect

project = Blueprint('project', __name__, template_folder='templates')
from src.main.modules.project.forms.add_project_form import AddProjectForm
from src.main.modules.project.decorators.project_owner import project_owner
from src.main.modules.project.project_service import ProjectService


@project.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = AddProjectForm()

    if not form.validate_on_submit():
        if request.method == 'POST':
            flash(message='Form error', category='error')

        return render_template('add-project.html', form=form)

    # put logics  here
    try:
        ProjectService.add_new_project(form)
        flash('Added', category='success')
        return redirect('/')
    except Exception as ex:
        print(ex)
        flash(message=ex, category='error')
        return redirect('/')



@project.route('/edit/<int:project_id>', methods=['GET', 'POST'])
@login_required
@project_owner
def edit(the_project):
    form = AddProjectForm()

    if not form.validate_on_submit():
        if request.method == 'POST':
            flash(message='Form error', category='error')

        # filling the old data to the form
        form.descriptions.data = the_project.descriptions
        form.name.data = the_project.name
        form.deadline.data = the_project.deadline
        return render_template('add-project.html', form=form)

    # put logics  here
    # checking if the deadline is smaller than any its children
    self_deadline = form.deadline.data
    invalid_tasks = list(filter(lambda task: task.deadline > self_deadline, the_project.tasks))
    print('invalid_tasks:', invalid_tasks)

    if len(invalid_tasks) > 0:
        form.deadline.errors.append('The deadline cannot smaller than its any children')
        flash('Form error', category='error')
        return render_template('add-project.html', form=form)

    try:
        ProjectService.update_project(form, the_project)
        flash('Updated', category='success')
        return redirect('/')
    except Exception as ex:
        print(ex)
        flash(message=ex, category='error')
        return redirect('/')


@project.route('/delete/<int:project_id>', methods=['GET', 'POST'])
@login_required
@project_owner
def delete(the_project):
    try:
        ProjectService.delete_project(the_project)
        flash('Removed', category='success')
        return redirect('/')
    except Exception as ex:
        print(ex)
        flash(message=ex, category='error')
        return redirect('/')

