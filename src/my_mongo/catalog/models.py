__author__ = 'johnb'

import datetime
from my_app import db


class Product(db.Document):
    created_at = db.DateTimeField(
        default=datetime.datetime.now, required=True
    )
    colorstyle = db.StringField(max_length=9, required=True)
    reshoot = db.StringField(max_length=1, required=False)
    username = db.StringField(max_length=44,required=False)
    photodate = db.StringField(max_length=30, required=False)

def __repr__(self):
    return '<Product %r>' % self.id