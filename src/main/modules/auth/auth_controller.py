from flask import Blueprint, jsonify, request, render_template
from werkzeug.security import generate_password_hash


# defining controller
from werkzeug.utils import redirect

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', static_url_path='auth/static')


@auth.route('/login', methods=['POST'])
def login():
    return "login page", 200


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return "logged out", 200


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    # grabbing the form
    from src.main.modules.auth.forms.signup_form import SignUpForm
    form = SignUpForm()

    # checking if is GET request
    if request.method == 'GET':
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
    password_hash = form.password.data

    new_user = User(email=email, full_name=fullName, password_hash=generate_password_hash(password_hash, method='sha256'))
    AuthService.register(new_user)

    return redirect(location='/')
    # return render_template("signup-success.html", email=email)


@auth.route('/reset-password', methods=['POST'])
def reset_password():
    from src.main.modules.auth.auth_service import AuthService

    AuthService.send_reset_password_email(request.email)
    return "password reset", 200
