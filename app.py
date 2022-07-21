from flask import Flask
from flask_minify import minify
from dotenv import load_dotenv
import os
import distutils.util 
import config
from views.website import website
from services.database import init_database

load_dotenv() 

def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", static_url_path="")
    minify(app=app, html=True, js=True, cssless=True, static=True)

    # set config
    if bool(distutils.util.strtobool(os.environ.get("SERVER_PRODUCTION"))):
        app.config.from_object(config.ProductionConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    #init services
    init_database(app)

    # register views
    app.register_blueprint(website)

    return app 

if __name__ == "__main__":
    app = create_app()
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
    