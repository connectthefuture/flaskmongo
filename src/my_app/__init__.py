__author__ = 'johnb'

from flask import Flask
from my_app.asset.views import asset_blueprint
app = Flask(__name__)
app.register_blueprint(asset_blueprint)
