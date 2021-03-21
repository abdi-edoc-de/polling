from flask import Flask
from polling.config import Config




def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(Config)


    from polling.main.routes import main
    app.register_blueprint(main)

    return app