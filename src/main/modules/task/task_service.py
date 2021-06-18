from src.app import db


class TaskService:

  @staticmethod
  def addNewTask(form):
    from src.main.modules.task.task_model import Task

    task = Task(
      name=form.name.data, 
      description = form.description.data, 
      user_id=form.user_id.data,
      priority_id = form.priority_id.data,
    )

    db.session.add(task)
    db.session.commit()

  @staticmethod
  def updateTask(oldTask):
    from src.main.modules.task.task_model import Task

    to_update_task = Task.query.get(oldTask.email)
    to_update_task.name = oldTask.name
    to_update_task.description = oldTask.description
    to_update_task.priority_od = oldTask.priority_id

    db.session.commit()
