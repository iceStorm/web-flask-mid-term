from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash


# self-created packages
# circular import error...
# from src.main.models.api_response import ApiResponse, ApiError
# from src.main.models.error_handlers import ErrorResponse
# from src.main.modules.auth.auth_service import AuthService
# from src.main.modules.user.user_model import User


# defining controller
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    return "login page", 200


@auth.route('/logout', methods=['POST'])
def logout():
    return "logged out", 200


@auth.route('/signup', methods=['POST'])
@cross_origin()
def signup():
    from src.main.models.api_response import ApiResponse, ApiError
    from src.main.models.error_handlers import ErrorResponse
    from src.main.modules.auth.auth_service import AuthService
    from src.main.modules.user.user_model import User

    json_body = request.get_json()
    email = json_body['email']
    fullName = json_body['fullName']
    password_hash = json_body['password']

    if AuthService.is_user_already_exists(email):
        return ErrorResponse\
            .CustomError(
                status_code=500,
                error=ApiError(
                    title='Already exists.',
                    message='There is an account registered with the email. Please try another email.')
            ).value

    new_user = User(email=email, full_name=fullName, password_hash=generate_password_hash(password_hash, method='sha256'))
    AuthService.register(new_user)

    return ApiResponse(status_code=200, data='Registered successfully.').value


@auth.route('/reset-password', methods=['POST'])
def reset_password():
    from src.main.modules.auth.auth_service import AuthService

    AuthService.send_reset_password_email(request.email)
    return "password reset", 200
