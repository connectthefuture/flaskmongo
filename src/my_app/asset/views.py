__author__ = 'johnb'

from werkzeug import abort
from flask import render_template
from flask import Blueprint
from my_app.asset.models import ASSETS
from my_app import db
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


@image_blueprint.route('/image/<colorstyle>')
def image(colorstyle):
   image = db['looklet_shot_list'].find_one_or_404({'_id': colorstyle})
   return render_template('lookletrecord.html', asset=image)

   #return 'Image - %s, $%s' % (image.name, image.md5)
   return 'Image - %s, $%s' % (image.colorstyle, image.username)


@image_blueprint.route('/imagefs/<filename>')
def imagefs(filename):
   image = db['fs.files'].find_one_or_404({'_id': filename})
   return render_template('image.html', image=image)

   return 'Image - %s, $%s' % (image.name, image.md5)
   #return 'Image - %s, $%s' % (image.colorstyle, image.username)

@image_blueprint.route('/images')
def images():
    images = db['fs.files'].findall()[:30]
    return render_template('image.html', images=images)

# import redis
# @image_blueprint.route('/image/<id>')
# def redis_image(id):
#    image = Image.query.get_or_404(id)
#    image_key = 'image-%s' % image.id
#    redis.set(image_key, image.name)
#    redis.expire(image_key, 600)
#    return 'Product - %s, $%s' % (image.name, image.md5)
