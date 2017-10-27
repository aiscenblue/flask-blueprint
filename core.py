import pkgutil
import os
import inspect

"""
    Description:: Initialize the blueprints inside in the root folder
    and sub folder

    Requirements:: all directories and sub directories must consist of __init__.py
    to be considered as a package. 

    files are ignored if its not end with .py or __.py

    NOTE :: directories must not consist of __ in their name

"""


class CoreBlueprint:
    __app = None

    def __init__(self, app, root_path):

        """ save sanic app module """
        self.__app = app
        self.root_path = root_path

        """ register blueprint to the current path """
        self.add_blueprint(root_path)

    def directory_path(self, path):

        """ get all the list of files and directories """
        for file in os.listdir(path):

            """ prevent __pycache__ directory or any directory that has __ """
            if "__" not in file:
                """ get the full path directory """
                dir_file = path + '/' + file

                """ check is the path is a directory 
                    only directories are picked
                """
                if os.path.isdir(dir_file):
                    """ register blueprint on the directory """
                    self.add_blueprint(dir_file)

                    """ find sub directories on each directory found """
                    self.directory_path(path=dir_file)

    @staticmethod
    def blueprint_name(name):
        """ set index automatically as home page """
        if "index" in name:
            name = str(name).replace("index", "")
        if "routes" in name:
            name = str(name).replace("routes", "")

        """ remove the last . in the string it it ends with a . 
            for the url structure must follow the flask routing format
            it should be /model/method instead of /model/method/
        """
        if name[-1:] == ".":
            name = name[:-1]
        http_name = str(name).replace(".", "/")
        print(http_name)
        return http_name

    @staticmethod
    def get_http_methods(names):
        if isinstance(names, list):
            methods = []

            for name in names:
                if "__" not in name:
                    if name == "index":
                        methods.append('GET')
                    elif name == "create":
                        methods.append('POST')
                    elif name == "update":
                        methods.append('PUT')
                    elif name == "destroy":
                        methods.append('DELETE')
                    else:
                        methods.append('GET')

            return methods
        else:
            raise TypeError("names must be a list")

    def model_add_router(self, mod):
        if hasattr(mod, '__routes__'):
            for route in mod.__routes__:
                if inspect.isclass(route[2]):
                    """ If it's a class it needs to extract the methods by function names
                        magic functions are excluded
                    """
                    route_name, slug, cls = route
                    for (fn_name, fn_object) in self.get_cls_fn_members(cls):
                        if inspect.isfunction(fn_object):
                            mod.__method__.add_url_rule(
                                rule=slug,
                                endpoint=fn_name,
                                view_func=fn_object,
                                methods=self.get_http_methods([fn_name]))
                        else:
                            raise KeyError("Member is not a function.")

                elif inspect.isfunction(route[2]):
                    route_name, slug, fn, methods = route

                    mod.__method__.add_url_rule(
                        rule=slug,
                        endpoint=fn.__name__,
                        view_func=fn,
                        methods=methods)

    @staticmethod
    def get_cls_fn_members(cls):
        return [member for member in inspect.getmembers(cls, predicate=inspect.isfunction)]

    def add_blueprint(self, path):

        """ find all packages in the current path """
        for loader, name, is_pkg in pkgutil.walk_packages(path, prefix="", onerror=None):
            """ if module found load module and save all attributes in the module found """
            mod = loader.find_module(name).load_module(name)

            """ find the attribute method on each module """
            if hasattr(mod, '__method__'):
                self.model_add_router(mod)
                root_module = self.root_path.replace(".", "")
                url_prefix_name = str(name).replace(root_module, "")
                """ register to the blueprint if method attribute found """
                self.__app.register_blueprint(mod.__method__, url_prefix=self.blueprint_name(url_prefix_name))

            else:
                """ prompt not found notification """
                # print('{} has no module attribute method'.format(mod))
                pass
