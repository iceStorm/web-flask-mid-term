from flask import Blueprint, render_template, g, current_app, request, jsonify, flash
from flask_login import current_user

# defining controller
# the static_url_path='home/static' means: this route has registered with url_prefix='/',
# so we need to add an alias name (will be displayed on the Browser's url bar)
# the alias 'home' here to prevent conflicting resource between the main app vs this route
indx = Blueprint('index', __name__, template_folder='templates', static_folder='static', static_url_path='home/static')


@indx.route("/", methods=["GET"])
def index():

    projects = []
    if current_user.is_authenticated:
        from src.main.modules.project.project_model import Project
        projects = Project.query.filter_by(user_id=current_user.email).all()

    return render_template('index.html', projects=projects)


@indx.route("/search", methods=["GET"])
def search():
    from src.main.modules.status.status_model import Status
    from src.main.modules.project.project_model import Project
    from src.main.modules.task.task_model import Task

    # querying all statuses
    statuses = Status.query.all()


    # request queries
    print(request.args)
    search_obj = request.args.get('search-obj')
    search_by = request.args.get('search-by')

    if search_obj and search_by:
        if search_by == '0':  # search by name
            name_query = request.args.get('search-name')
            if name_query:

                results = []
                searching_type = '___'

                if search_obj == '0':
                    searching_type = 'projects'
                    results = Project.query.filter(
                        Project.user_id == current_user.email,
                        Project.name.ilike(f'%{name_query}%')).all()
                else:
                    searching_type = 'tasks'
                    results = Task.query.filter(Task.descriptions.ilike(f'%{name_query}%')).all()
                    results = list(filter(lambda task: task.project.user_id==current_user.email, results))

                return render_template('index.html', projects=results, tasks=results, searching_type=searching_type)

        else:  # search by status
            status_id = request.args.get('search-status')
            if status_id:

                results = []
                searching_type = '___'

                if search_obj == '0':
                    searching_type = 'projects'
                    results = Project.query.filter_by(user_id=current_user.email, status_id=status_id).all()
                else:
                    searching_type = 'tasks'
                    results = Task.query.filter(Task.status_id == status_id).all()
                    results = list(filter(lambda task: task.project.user_id==current_user.email, results))

                return render_template('index.html', projects=results, tasks=results, searching_type=searching_type)
