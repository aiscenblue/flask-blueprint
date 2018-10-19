from .package_extractor import PackageExtractor

"""
    Description:: Initialize the blueprints inside in the root folder
    and sub folder

    Requirements:: all directories and sub directories must consist of __init__.py
    to be considered as a package. 

    files are ignored if its not end with .py or __.py

    NOTE :: directories must not consist of __ in their name

"""

__all__ = ['Core']
__version__ = '1.2.4'


"""
    Core
        :param app
            your flask application module
                example: app = Flask('my_flask_app')
        
        :param root_paths
            paths for your module directories        

"""


class Core:
    __app = None

    def __init__(self, app, root_paths):

        """ save flask app module """
        self.__app = app
        self.root_path = root_paths

        """ register blueprint to the current path """
        PackageExtractor(application=app, paths=root_paths)
