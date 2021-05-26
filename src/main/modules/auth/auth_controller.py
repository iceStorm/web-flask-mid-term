from flask import Blueprint, jsonify, request, render_template, flash
from flask_login import login_required, current_user, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect


# defining controller
auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', static_url_path='auth/static')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # grabbing the form
    from src.main.modules.auth.forms.login_form import LoginForm
    form = LoginForm()

    # checking if is GET request
    if request.method == 'GET':
        # redirecting logged-in user to the index page
        if current_user.is_authenticated:
            flash('You\'re already logged in!', category='warning')
            return redirect('/')
        return render_template('login.html', form=form)

    # checking if the form is not valid yet
    if not form.validate_on_submit():
        return render_template('login.html', form=form)

    from src.main.modules.user.user_model import User
    user = User.query.get(form.email.data)

    # let's log the user in
    login_user(user, remember=form.remember)
    return redirect(location='/')


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(location="/")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    # grabbing the form
    from src.main.modules.auth.forms.signup_form import SignUpForm
    form = SignUpForm()

    # checking if is GET request
    if request.method == 'GET':
        # redirecting logged-in user to the index page
        if current_user.is_authenticated:
            flash('Please logout first, then signup!', category='warning')
            return redirect('/')
        return render_template('signup.html', form=form)

    # checking if the form is not valid yet
    if not form.validate_on_submit():
        return render_template('signup.html', form=form)

    # all validation passed, let's continue handle the process
    from src.main.modules.auth.auth_service import AuthService
    from src.main.modules.user.user_model import User

    # grabbing form fields data
    email = form.email.data
    fullName = form.full_name.data
    password = form.password.data

    # creating a new user based-on the Form's data
    new_user = User(email=email, full_name=fullName, password_hash=generate_password_hash(password, method='sha256'))
    AuthService.register(new_user)

    # showing a flash message -> redirecting to the home page
    flash(message='Successfully registered!', category='success')
    return redirect(location='/')


@auth.route('/reset-password', methods=['POST'])
def reset_password():
    from src.main.modules.auth.auth_service import AuthService

    AuthService.send_reset_password_email(request.email)
    return "password reset", 200
