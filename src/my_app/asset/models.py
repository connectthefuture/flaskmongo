__author__ = 'johnb'

__author__ = 'johnb'

import datetime
from my_app import db


class Image(db.Document):
    created_at = db.DateTimeField(
        default=datetime.datetime.now, required=True
    )
    colorstyle = db.StringField(max_length=9, required=True)
    reshoot = db.StringField(max_length=1, required=False)
    username = db.StringField(required=False)
    md5 = db.StringField(required=False)


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

