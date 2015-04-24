#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup

setup(
   name = 'my_app',
   version='1.7.2',
   license='MIT License',
   author='john bragato',
   author_email='jb@relic7.org',
   description='Application for Flask',
   packages=['my_app'],
   platforms='any',
   install_requires=[
        'flask',
        'requests',
        'Jinja2',
        'pymongo',
        'itsdangerous',
        'Werkzeug'
    ],
   classifiers=[
       'Development Status :: 4 - Beta',
       'Environment :: Web Environment',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: MIT License',
       'Operating System :: OS Independent',
       'Programming Language :: Python',
       'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
       'Topic :: Software Development :: Libraries :: Python Modules'
   ],
)
