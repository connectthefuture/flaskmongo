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


    def __repr__(self):
        return '<Image %r>' % self.id


