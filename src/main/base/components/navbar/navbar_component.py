from flask import request, render_template
from .navbar_viewmodel import NavBarViewModel, NavItem
from flask_login import current_user


def get_view_model() -> NavBarViewModel:
    """
    Resetting the nav items active state, load the current_user
    """
    # print('current_user inside NavBar component:', current_user)

    return NavBarViewModel(
        user=current_user,
        nav_items=[
            NavItem(href='/', title='Home', is_active=False),
            NavItem(href='/projects', title='Projects', is_active=False),
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
