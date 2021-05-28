export APP_CONFIG_FILE=config/development.py
export FLASK_ENV=development
export FLASK_APP=src/app.py

# adding paths
ROOT_DIR=.
MAIN_DIR=./src/main/
export PYTHONPATH=$MAIN_DIR:$ROOT_DIR

#export

#flask db init
#flask db migrate -m "create table users"
flask db upgrade