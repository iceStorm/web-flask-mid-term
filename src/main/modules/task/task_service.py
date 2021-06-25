from src.app import db


class TaskService:
    @staticmethod
    def get_tasks_by(user_id, trashed, done, per_page=5, page_index=1):
        from src.main.modules.task.task_model import Task

        paginator = Task.query\
                .filter_by(user_id=user_id, trashed=trashed, done=done)\
                .paginate(page=page_index, max_per_page=per_page)\

        # print(paginator)
        return paginator


    @staticmethod
    def add_new_task(form):
        from src.main.modules.task.task_model import Task

        task = Task(
            name=form.name.data,
            description=form.description.data,
            user_id=form.user_id.data,
            priority_id=form.priority_id.data,
            trashed=False,
            done=False,
        )

        db.session.add(task)
        db.session.commit()


    @staticmethod
    def duplicate_task(old_task):
        from src.main.modules.task.task_model import Task

        task = Task(
            name=old_task.name,
            description=old_task.description,
            user_id=old_task.user_id,
            priority_id=old_task.priority_id,
            trashed=False,
            done=False,
        )

        db.session.add(task)
        db.session.commit()


    @staticmethod
    def update_task(task_id, form):
        from src.main.modules.task.task_model import Task
        to_update_task = Task.query.get(task_id)

        to_update_task.name = form.name.data
        to_update_task.description = form.description.data
        to_update_task.priority_id = form.priority_id.data

        db.session.commit()


    @staticmethod
    def move_to_trash(the_task):
        """
        Moving the task to the Trash.
        @param the_task: the task to be moved.
        """
        the_task.trashed = True
        db.session.commit()


    @staticmethod
    def restore_from_trash(the_task):
        """
        Restoring the task from the Trash.
        @param the_task: the task to be restoring.
        """
        the_task.trashed = False
        db.session.commit()


    @staticmethod
    def remove_task(the_task):
        """
        Actually remove the trahs from the database.
        @param the_task: the task to be removed.
        """
        db.session.delete(the_task)
        db.session.commit()
