from flask import Flask
from datetime import datetime, time
from flask_sqlalchemy import SQLAlchemy
from project.utils import CustomJSONEncoder

db = SQLAlchemy()

def create_app():
    # instantiate the app
    app = Flask(__name__)
    # Set custom encoder
    app.json_encoder = CustomJSONEncoder
    # set config
    app.config.from_object('project.config.BaseConfig')

    db.init_app(app)
    #Setting blueprints for interacting with DB objects
    from project.jobs import jobs_blueprint
    app.register_blueprint(jobs_blueprint)
    from project.users import users_blueprint
    app.register_blueprint(users_blueprint)

    @app.route("/")
    def testing():
        return "<h1 style='color:blue'>Lets Flask!</h1>"

    return app



