from flask import Flask


class App(Flask):
    def __init__(self, instance_path):
        super(App, self).__init__(
            import_name=__name__,
            instance_path=instance_path,
            instance_relative_config=True,
        )

        # assigning the base templates & static folder
        self.template_folder = './base/templates'
        self.static_folder = './base/static'

        self.load_environment_variables()
        self.register_blueprints()
        self.register_error_handlers()

    def load_environment_variables(self):
        """
        Loading the configured environment variables.
        """
        # Load the default configuration (../config/default.py)
        self.config.from_object('config.default')

        # Load the configuration from the instance folder --- overriding the above
        self.config.from_pyfile('./instance/config.py')

        # Load the file specified by the APP_CONFIG_FILE environment variable
        # Variables defined here will override those in the default configuration
        self.config.from_envvar('APP_CONFIG_FILE')

    def register_blueprints(self):
        """
        Registering the app's blueprints.
        """
        from modules.index.index_controller import indx
        from modules.auth.auth_controller import auth

        self.register_blueprint(indx, url_prefix="/")
        self.register_blueprint(auth, url_prefix="/")

    def error_handlers(self, status_code: int):
        pass

    def register_error_handlers(self):
        """
        Registering custom error handlers that show custom view (html page) for the app.
        """
        from src.main.error_handlers import ErrorHandler

        self.register_error_handler(403, ErrorHandler.forbidden)
        self.register_error_handler(404, ErrorHandler.not_found)
        self.register_error_handler(500, ErrorHandler.server_error)
