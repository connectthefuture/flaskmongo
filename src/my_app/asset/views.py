__author__ = 'johnb'

from werkzeug import abort
from flask import render_template
from flask import Blueprint
from my_app.asset.models import ASSETS

asset_blueprint = Blueprint('asset', __name__)


@asset_blueprint.route('/')
@asset_blueprint.route('/home')
def home():
    return render_template('home.html', assets=ASSETS)


@asset_blueprint.route('/asset/<key>')
def asset(key):
    asset = ASSETS.get(key)
    if not asset:
        abort(404)
    return render_template('asset.html', asset=asset)