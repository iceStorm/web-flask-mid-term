from flask import Blueprint, render_template, g, current_app


# defining controller
indx = Blueprint('index', __name__, template_folder='templates')


@indx.route("/")
def index():
    return render_template('index.html', title='Todo')


@indx.route("/<slug>")
def page(slug):
    return render_template('index.html', value=slug)
