import os
from flask import Flask

from data import Store
from development import DEBUG

app = Flask(__name__, static_url_path='')
app.debug = DEBUG

@app.route('/')
def hello():
    foo = Store.get('foo')
    body = 'app.debug = %s\nHello World! Foo is currently %s' % (app.debug, foo)
    return app.jinja_env.get_template('root.html').render(Title='Moonbeam - Home', Test=body)