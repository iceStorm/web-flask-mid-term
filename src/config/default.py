#   default environment variables for use both in production & development,
#   the variables that don't need to changed between environments should be only placed here.
#


APP_NAME = "Todo-List App"

SECRET_KEY = "iceStorm"
BCRYPT_LOG_ROUNDS = 12

# get called in the App class's load_environment_variables()
SQLALCHEMY_DATABASE_URI = 'sqlite:///../../db/app.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = True
