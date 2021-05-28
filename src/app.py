# standard libs
import sys
import os
from pathlib import Path


def add_sys_paths():
    print('\n[ADDING PATHS TO THE PYTHON ENVIRONMENT...]')

    # getting the current file's absolute path
    CURRENT_FILE_ABSOLUTE_PATH = Path(__file__).absolute()

    # WORKING_DIR: src
    WORKING_DIR = os.path.abspath(os.path.join(CURRENT_FILE_ABSOLUTE_PATH, '../'))

    # ROOT_DIR (includes the: src ; scripts ; venv ; ..
    ROOT_DIR = os.path.abspath(os.path.join(CURRENT_FILE_ABSOLUTE_PATH, '../../'))

    # appending the WORKING_DIR, ROOT_DIR to the python environment
    sys.path.append(WORKING_DIR)
    sys.path.append(ROOT_DIR)
    print('\n[PATHS IN THE PYTHON ENVIRONMENT...]:\n', '\n'.join(sys.path), '\n')

    return WORKING_DIR, ROOT_DIR


def ensure_tables():
    import main.modules.user.user_model as user_model

    # [only need/must] to call the last imported one to invoke the ensure() function
    user_model.ensure()


def show_message(message: str):
    if __name__ == "__main__":
        print(message)


def create_app():
    # initializing the app
    print("\n[INITIALIZING THE APP...]")
    from main import App
    app = App(instance_path=add_sys_paths()[0])

    # migrating Models to DB
    from flask_migrate import Migrate
    import main.modules.user.user_model as user_model
    from main.modules.user.user_model import User
    migrate = Migrate()
    migrate.init_app(app, db)

    print("\n[INITIALIZING THE DATABASE...]")
    db.init_app(app=app)

    app.register_cors(app_instance=app)

    # ensuring the tables is exist or create new ones
    # with app.app_context():
    #     print("\n[ENSURING THE DATABASE...]")
    #     ensure_tables()

    return app


# defining the db instance
show_message("\n[DEFINING THE DATABASE INSTANCE...]")
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


# the App's entry point
# function calls should be wrapped here, preventing: import-auto executing
if __name__ == "__main__":
    app = create_app()

    print("\n[RUNNING...]")
    app.run()