__author__ = 'johnb'

from werkzeug import abort
from flask import render_template
from flask import Blueprint
from my_app.asset.models import ASSETS

asset_blueprint = Blueprint('product', __name__)


@asset_blueprint.route('/')
@asset_blueprint.route('/home')
def home():
    return render_template('home.html', assets=ASSETS)


@asset_blueprint.route('/product/<key>')
def asset(key):
    asset = ASSETS.get(key)
    if not asset:
        abort(404)
    return render_template('asset.html', asset=asset)




from my_app.asset.models import Image

image_blueprint = Blueprint('image', __name__)


@image_blueprint.route('/image')
@image_blueprint.route('/image_home')
def image_home():
   return "Welcome to the Image Home."


@image_blueprint.route('/image/<key>')
def image(key):
   image = Image.objects.get_or_404(key=key)
   return 'Image - %s, $%s' % (image.name, image.md5)

@image_blueprint.route('/images')
def images():
    images = Image.objects.all()


import redis
@image_blueprint.route('/image/<id>')
def redis_image(id):
   image = Image.query.get_or_404(id)
   image_key = 'image-%s' % image.id
   redis.set(image_key, image.name)
   redis.expire(image_key, 600)
   return 'Product - %s, $%s' % (image.name, image.md5)
