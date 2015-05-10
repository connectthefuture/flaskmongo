__author__ = 'johnb'

import datetime
from my_app import db
db = db.connect()

col = db['images'] #['looklet_shot_list']

from flask_mongoengine import MongoEngine, Document
#dstr = MongoEngine.DynamicDocument
class Image(Document):
    #pass
    id = Document.StringField
    created_at = Document.StringField(default=datetime.datetime.now, required=True)
    colorstyle = Document.StringField(max_length=9, required=True)
    reshoot = Document.StringField(max_length=1, required=False)
    username = Document.StringField(required=False)
    timestamp = Document.StringField(required=False)

    def __repr__(self):
        return '<Image %r>' % self.id



ASSETS = {
    'iphone': {
        'name': 'iPhone 5S',
        'category': 'Phones',
        'price': 699,
    },
    'galaxy': {
        'name': 'Samsung Galaxy 5',
        'category': 'Phones',
        'price': 649,
    },
    'ipad-air': {
        'name': 'iPad Air',
        'category': 'Tablets',
        'price': 649
    }
}

