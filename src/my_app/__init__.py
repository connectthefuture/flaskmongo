__author__ = 'johnb'

from flask import Flask
from my_app.asset.views import asset_blueprint
app = Flask(__name__,
            static_url_path='/static',
            static_folder='static'
            )
app.config.from_object('my_app.config')
app.register_blueprint(asset_blueprint)
