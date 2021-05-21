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

        self.register_blueprint(indx)
