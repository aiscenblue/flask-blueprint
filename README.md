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
    from flask_blueprint import Core
    
    Core(app='flask/application/app', root_path='path/to/module')
```

> view on pypi

> https://pypi.python.org/pypi/flask-blueprint

# Module routing


` create a folder Home where you point your module directory`

```
~/module-directory/
    |-- /module_name
      |-- __init__.py
      |-- methods.py
      |-- routes.py
```

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
