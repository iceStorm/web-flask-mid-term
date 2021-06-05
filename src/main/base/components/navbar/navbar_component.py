from flask import request, render_template
from flask_login import current_user

from .navbar_viewmodel import NavBarViewModel, NavItem

# import this model to handle the DB (Flask-SQLAlchemy)
from src.main.modules.user.user_model import User


def get_view_model() -> NavBarViewModel:
    """
    Resetting the nav items active state, load the current_user
    """
    print('current_user inside NavBar component:', current_user.get_id())

    full_name = ''  # this will be hidden on the navbar if no user is logged in
    if current_user.is_authenticated:
        full_name = User.query.get(current_user.get_id()).full_name

    return NavBarViewModel(
        user=current_user,
        full_name=full_name,
        nav_items=[
            NavItem(href='/', title='Home'),
            NavItem(href='/projects', title='Projects'),
            NavItem(href='/projects', title='Organizations'),
            NavItem(href='/projects', title='Calendar'),
        ],
    )


def navbar_component():
    def component():
        # getting a new view model instance
        vm = get_view_model()

        # getting current requesting path
        req_path = request.path
        print('req path:', req_path)

        # setting the current active page
        vm.set_active_nav_item(path=req_path)
        return render_template("navbar.html", vm=vm)

    return dict(navbar_component=component)
