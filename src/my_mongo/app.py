__author__ = 'johnb'

from flask import Flask

# App
app = Flask(
    __name__,
    static_url_path = '/static',
    static_folder = str(__name__) + '/static'
)
app.config.from_object('my_mongo.config')

## DB
from flask.ext.mongoengine import MongoEngine
from redis import Redis
app.config['MONGODB_SETTINGS'] = {'DB': 'images'}
db = MongoEngine(app)
redis = Redis()

# Model views
from my_mongo.product.views import image
app.register_blueprint(image)