# Easy Installation

```
    CoreBlueprint(app='flask/application/app', root_path='path/to/module')
```

# Module routing


> create a folder Home where you point your module directory

```
root-directory/
    __init__.py
    methods.py
    routes.py
```

`NOTE:: __init__.py must be ALWAYS included in the folder in order to detect the model folder as a module`

> methods.py

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

> routing.py

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