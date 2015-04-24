#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode
from bson.objectid import ObjectId
from bson.errors import InvalidId

class ObjectIDConverter(BaseConverter):
    def to_python(self, value):
        try:
            return ObjectId(base64_decode(value))
        except (InvalidId, ValueError, TypeError):
            raise ValidationError()
    def to_url(self, value):
        return base64_encode(value.binary)




#
# class CounterAPI(MethodView):
#
#     def get(self):
#         return session.get('counter', 0)
#
#     def post(self):
#         session['counter'] = session.get('counter', 0) + 1
#         return 'OK'
#
# app.add_url_rule('/counter', view_func=CounterAPI.as_view('counter'))
