from flask import Flask
from flask_session import Session # type: ignore
from .config import Config # type: ignore


def create_app():
    app= Flask (__name__)
    app.config.from_object(Config)

    Session(app)

    from .route import main
    app.register_blueprint(main)
    
    return app