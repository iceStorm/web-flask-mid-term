from flask import request, render_template
from .navbar_viewmodel import NavBarViewModel, NavItem

view_model = NavBarViewModel(
    is_user_logged_in=False,
    nav_items=[
        NavItem(href='/', title='Home', is_active=False),
        NavItem(href='/login', title='Login', is_active=False),
        NavItem(href='/signup', title='Sign Up', is_active=False)
    ],
)


def component():
    req_path = request.path

    for item in view_model.nav_items:
        if item.href == req_path:
            item.is_active = True

    return render_template("navbar.html", vm=view_model)


def navbar_component():
    return dict(navbar_component=component)
