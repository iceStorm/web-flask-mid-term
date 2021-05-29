export APP_CONFIG_FILE=config/development.py
export FLASK_ENV=development

ROOT_DIR=.
MAIN_DIR=./src/main/
export PYTHONPATH=$MAIN_DIR:$ROOT_DIR

export # showing all environment variables

cd $OLDPWD # going out to the root folder
python src/app.py
