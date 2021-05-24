import json
import time

from flask import Blueprint, render_template, g, current_app, request, jsonify

# defining controller
# the static_url_path='home/static' means: this route has registered with url_prefix='/',
# so we need to add an alias name (will be displayed on the Browser's url bar)
# the alias 'home' here to prevent conflicting resource between the main app vs this route
indx = Blueprint('index', __name__, template_folder='templates', static_folder='static', static_url_path='home/static')


@indx.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html', value='Todo')

