import os
from injector import Binder
from flask_injector import FlaskInjector, singleton, request
from flask import render_template
from connexion.resolver import RestyResolver
import config
from injector import inject
from flask_jwt import JWT, jwt_required, current_identity



app = config.app
app.add_api('app.yml', resolver=RestyResolver('api'))

@app.route("/")
def home():
    return "Success"
