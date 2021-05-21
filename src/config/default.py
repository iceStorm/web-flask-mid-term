#   default environment variables for use in production,
#   the variables that don't need to changed between environments should be only placed here.
#


APP_NAME = "RS-Tree"

SECRET_KEY = "iceStorm"

# Configuration for the Flask-Bcrypt extension
BCRYPT_LOG_ROUNDS = 12
SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = True
