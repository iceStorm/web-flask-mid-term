from flask import Blueprint, render_template, redirect
from flask.globals import current_app, request
from flask.helpers import flash
from flask_login import login_required, current_user

task = Blueprint('task', __name__, template_folder='templates')
from src.main.modules.task.forms.add_new_form import AddNewTaskForm
from src.main.modules.task.task_service import TaskService


@task.route('/add-new', methods=['GET', 'POST'])
@login_required
def addNew():
  form = AddNewTaskForm()

  # filling the priority choices
  from src.main.modules.priority.priority_model import Priority
  form.priority_id.choices = [(p.id, p.name) for p in Priority.query]


  if request.method == 'GET':
    # re-assigning the email (id) to the form
    form.user_id.data = current_user.email
    return render_template('add-new.html', form=form)
  

  # validate the form
  if not form.validate_on_submit():
    flash('Form error!', category='error')

    # re-assigning the email (id) to the form
    form.user_id.data = current_user.email
    return render_template('add-new.html', form=form)


  # all done. let's handle the main process
  from src.main.modules.task.task_service import TaskService
  import sys

  try:
    TaskService.addNewTask(form=form)
    flash('Ok', category='success')
    return redirect('/')
  except NameError as err:
    flash('Error occurred when adding the Task', category='error')
    print('error', err)
    return render_template('add-new.html', form=form)


@task.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit(task_id):
  # filling the priority choices
  form = AddNewTaskForm()
  from src.main.modules.priority.priority_model import Priority
  form.priority_id.choices = [(p.id, p.name) for p in Priority.query]


  if request.method == 'GET':
    from src.main.modules.task.task_model import Task
    the_task = Task.query.get(task_id)

    form.user_id.data = the_task.user_id
    form.name.data = the_task.name
    form.description.data = the_task.description
    form.priority_id.data = the_task.priority_id

    return render_template('add-new.html', isEditing=True, form=form)


  # on post request
  if not form.validate_on_submit():
    flash('Form error!', category='success')
    return render_template('add-new.html', isEditing=True, form=form)

  try:
    TaskService.updateTask(the_task)
    flash('Updated!', category='success')
    return redirect('/')
  except:
    import sys
    print('\n\n\nerror', sys.exc_info[0])

    flash('Form error!', category='error')
    return render_template('add-new.html', isEditing=True, form=form)
