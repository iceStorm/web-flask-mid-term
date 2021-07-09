from flask_login import current_user

from src.app import db


class TaskService:

    # @staticmethod
    # def get_tasks_by(user_id, trashed, done=-1, per_page=20, page_index=1):
    #     from src.main.modules.task.task_model import Task
    #     paginator = None
    #
    #     if not done or done == -1:
    #         paginator = Task.query \
    #             .filter_by(user_id=user_id, trashed=trashed) \
    #             .paginate(page=page_index, max_per_page=per_page) \
    #
    #     else:
    #         paginator = Task.query\
    #             .filter_by(user_id=user_id, trashed=trashed, done=done)\
    #             .paginate(page=page_index, max_per_page=per_page)\
    #
    #     # print(paginator)
    #     return paginator


    @staticmethod
    def add_new_task(form):
        from src.main.modules.task.task_model import Task

        task = Task(
            descriptions=form.descriptions.data,
            deadline=form.deadline.data,

            priority_id=form.priority_id.data,
            project_id=form.project_id.data,
            status_id=4,
        )

        db.session.add(task)
        db.session.commit()
        TaskService.update_project_status(task.project)


    @staticmethod
    def update_task(the_task, form):
        the_task.descriptions = form.descriptions.data
        the_task.deadline = form.deadline.data

        the_task.priority_id = form.priority_id.data
        the_task.status_id = form.status_id.data
        the_task.project_id = form.project_id.data

        db.session.commit()
        TaskService.update_project_status(the_task.project)


    @staticmethod
    def remove_task(the_task):
        """
        Actually remove the trahs from the database.
        @param the_task: the task to be removed.
        """
        the_project = the_task.project
        db.session.delete(the_task)

        db.session.commit()
        TaskService.update_project_status(the_project)


    @staticmethod
    def update_project_status(the_project):
        if len(the_project.tasks) < 1:
            # status_id == 4 == not_started
            the_project.status_id = 4
            db.session.commit()
            return

        # status_id == 2 == overdue
        overdue_tasks_count = list(filter(lambda task: task.status_id == 2, the_project.tasks))
        # when any overdue tasks have found, regardless any finished or in_progress tasks
        if len(overdue_tasks_count) > 0:
            the_project.status_id = 2
            db.session.commit()
            return

        # status_id == 3 == in_progress
        in_progress_tasks = list(filter(lambda task: task.status_id == 3, the_project.tasks))
        if len(in_progress_tasks) > 0:
            the_project.status_id = 3
            db.session.commit()
            return

        # status_id == 1 == finished
        finished_tasks_count = list(filter(lambda task: task.status_id == 1, the_project.tasks))
        # when all the tasks have finished
        if len(finished_tasks_count) == len(the_project.tasks):
            the_project.status_id = 1
            db.session.commit()
            return

        # otherwise
        # status_id == 4 == not_started
        the_project.status_id = 4
        db.session.commit()
