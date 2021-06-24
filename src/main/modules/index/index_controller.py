from flask import Blueprint, render_template, g, current_app, request, jsonify, flash
from flask_login import current_user

# defining controller
# the static_url_path='home/static' means: this route has registered with url_prefix='/',
# so we need to add an alias name (will be displayed on the Browser's url bar)
# the alias 'home' here to prevent conflicting resource between the main app vs this route
indx = Blueprint('index', __name__, template_folder='templates', static_folder='static', static_url_path='home/static')


@indx.route("/", methods=["GET"])
def index():
    tasks = []

    if current_user.is_authenticated:
        per_page = request.args.get('per_page')
        page_index = request.args.get('page_index')

        from src.main.modules.task.task_service import TaskService
        tasks = TaskService.get_tasks_by(
            user_id=current_user.email,
            trashed=False,
            done=False,
            per_page=int(per_page or 5),
            page_index=int(page_index or 1)
        )

    return render_template('index.html', tasks=tasks)
