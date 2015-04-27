__author__ = 'johnb'

from werkzeug import abort
from flask import render_template

from flask import request, Blueprint, jsonify
from my_mongo.product.models import Image

product = Blueprint('image', __name__)


@product.route('/')
@product.route('/home')
def home():
   return "Welcome to the Product Home."


@product.route('/image/<key>')
def image(key):
   image = Image.objects.get_or_404(key=key)
   return 'Image - %s, $%s' % (image.name, image.price)

@product.route('/images')
def images():
    images = Image.objects.all()