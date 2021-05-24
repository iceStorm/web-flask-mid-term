import json
import time

from flask import Blueprint, render_template, g, current_app, request, jsonify

# defining controller
indx = Blueprint('index', __name__, template_folder='templates', static_folder='index/static')


@indx.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html', value='Todo')

