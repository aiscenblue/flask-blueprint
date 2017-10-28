from package_extractor import PackageExtractor

"""
    Description:: Initialize the blueprints inside in the root folder
    and sub folder

    Requirements:: all directories and sub directories must consist of __init__.py
    to be considered as a package. 

    files are ignored if its not end with .py or __.py

    NOTE :: directories must not consist of __ in their name

"""


class Core:
    __app = None

    def __init__(self, app, root_path):

        """ save sanic app module """
        self.__app = app
        self.root_path = root_path

        """ register blueprint to the current path """
        PackageExtractor(application=app, path=root_path)
