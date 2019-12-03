# Program Name: request_data_from_kaggle
# Purpose: Flask application to serve web pages with charts and statistically information

from flask import Flask
from views.routes import routes_blueprint
from database.database import db

import os.path
import logging
from dataset.request_dataset_from_kaggle import request_csv_file


def create_app():
    # Creating an instance of the Flask class
    app = Flask(__name__)
    # Pulling in configuration of database
    app.config.from_pyfile('config.cfg')
    db.init_app(app)
    # Registering blueprint for routes in flask
    app.register_blueprint(routes_blueprint)
    return app


def setup_database(app):
    # Creating all the tables in database
    with app.app_context():
        db.create_all()


# Logging setup with basic configuration, output to file (example.log)
def logging_setup():
    logging.basicConfig(filename='example.log', filemode='w', format='%(levelname)s:%(message)s', level=logging.DEBUG)


# Running the application
if __name__ == "__main__":
    # Request to download csv file
    request_csv_file()
    app = create_app()
    # Because this is just a demonstration we set up the database like this.
    if not os.path.isfile('fifa.db'):
        setup_database(app)
    app.run()
    logging_setup()
