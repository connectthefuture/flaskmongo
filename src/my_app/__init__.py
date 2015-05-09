__author__ = 'johnb'

from flask import Flask
app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object('my_app.config')



########
## DB ##
from flask_mongoengine import MongoEngine
#from redis import Redis
app.config['MONGODB_SETTINGS'] = {
                                  'DB': 'gridfs_mrktplce',
                                  #'DB': 'images',
                                  #'HOST': 'mongodb://relic7:mongo7@ds031591.mongolab.com:31591/images'
                                  'HOST': 'mongodb://relic7:mongo7@ds031852.mongolab.com:31852/gridfs_mrktplce'
                                  }
#app.config['MONGODB_SETTINGS'] = {'DB': 'gridfs_mrktplce'}
db = MongoEngine(app)
#redis = Redis()


#### Register Models/Blueprints
from my_app.asset.views import image_blueprint
from my_app.asset.views import asset_blueprint

app.register_blueprint(image_blueprint)
app.register_blueprint(asset_blueprint)
