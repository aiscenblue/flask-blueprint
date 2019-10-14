# Flask Blueprint
Better way to create blueprint

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/aiscenblue/flask-blueprint)
[![PyPI version](https://badge.fury.io/py/flask-app-core.svg)](https://github.com/aiscenblue/flask-blueprint)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://github.com/aiscenblue/flask-blueprint/blob/master/LICENSE)

# Requirements:
```
  Python 2.7 or higher
```

# PIP installation

`pip install flask-blueprint`

# Easy Installation

```
    from flask_blueprint import Blueprint
    from flask import Flask
    
    flask_app = Flask(import_name, instance_relative_config=True)
    Blueprint(app=flask_app, root_path=['path/to/module'])
    flask_app.run()
```

> view on pypi

> https://pypi.python.org/pypi/flask-blueprint

# Simple Routing
```
create a /modules directory
create index.py under modules directory
paste the code below to create initial route
```

    from flask import Blueprint, make_response, render_template

    """ blueprint module for url handler """
    __method__ = Blueprint(__name__, __name__)
    app = __method__
    
    
    @app.route("/", methods=['GET'])
    def index():
        return make_response("Welcome to flask starter kit API!", 200)

# Class routing


` create a folder Home where you point your module directory`

```
~/module-directory/
  /__init__.py
  /index.py 
```
`Your index.py will be your initial route.`

`FOR MORE EXAMPLE SEE: `[Flask Starter kit](https://github.com/aiscenblue/flask-starter-kit)

`NOTE:: __init__.py must be ALWAYS included in the folder in order to detect the model folder as a module`

#### methods.py

```
from flask import make_response


class Methods:

    @staticmethod
    def index():
        return make_response("Welcome module", 200)

    @staticmethod
    def create():
        return make_response("Welcome POST method", 200)

    @staticmethod
    def update():
        return make_response("Welcome PUT method", 200)

    @staticmethod
    def destroy():
        return make_response("Welcome DELETE method", 200)

```

#### routing.py

```
from flask import Blueprint
from module.welcome.methods import Methods

""" blueprint module for url handler """
__method__ = Blueprint(__name__, __name__)

""" 
    ROUTES:
        routing for base directory module
        name, slug, function, methods
"""
__routes__ = [
    ("welcome", "/", Methods)
]

```

# Variable Rules
`http://flask.pocoo.org/docs/0.12/quickstart/#variable-rules`
```
__routes__ = [
    ("posts", "/<int:post_id>", Methods)
]
```

```
from flask import make_response


class Methods:

    @staticmethod
    def index(post_id=None):
        return make_response("get post ID: {}".format(post_id), 200)

    @staticmethod
    def create(name=None):
        return make_response("POST method for post ID: {}".format(post_id), 200)

    @staticmethod
    def update(name=None):
        return make_response("PUT method for post ID: {}".format(post_id), 200)

    @staticmethod
    def destroy(name=None):
        return make_response("DELETE method for post ID: {}".format(post_id), 200)

```

# Custom Routing using function

```
from flask import Blueprint
from module.welcome.methods import Methods

""" blueprint module for url handler """
__method__ = Blueprint(__name__, __name__)

""" 
    ROUTES:
        routing for base directory module
        name, slug, function, methods
"""
__routes__ = [
    ("welcome", "/", Methods.my_new_function, ['GET', 'POST', 'PUT', 'DELETE'])
]
```

#### you can set a function with single or multiple methods

#### blueprint documentation
#### http://flask.pocoo.org/docs/0.12/blueprints/#my-first-blueprint
