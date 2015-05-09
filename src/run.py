__author__ = 'johnb'

from my_app import app
host = '0.0.0.0'
app.run(host=host,
        use_reloader=True)