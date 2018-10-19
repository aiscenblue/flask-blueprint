import inspect
import pkgutil
from os import listdir

from .module_router import ModuleRouter

"""
    PACKAGE EXTRACTOR

        It's purpose is to extract all the modules based on the paths of the parameter given
        it extracts valid packages within the root module path
        and register the valid modules to the flask blueprint

    :param application
        flask application object
            example: flask_app = Flask(import_name, instance_relative_config=True)
            application=flask_app
    :param paths
        paths are a list of directories within your application root folder
            example:
                paths = ['path/to/your/application/modules']
"""


class PackageExtractor:
    __packages = None
    __modules = []
    __routers = []

    def __init__(self, application, paths):
        self.paths = paths
        self.application = application
        self.__iter_paths()

    def __iter_paths(self):
        for path in self.paths:
            self.__iter_path_sub_path(sub_paths=listdir(path))

    def __iter_path_sub_path(self, sub_paths):
        for path_directories in sub_paths:
            self.__extract_packages(packages=pkgutil.walk_packages(path_directories, prefix='', onerror=None))

    def __extract_packages(self, packages):
        if inspect.isgenerator(packages):
            try:
                loader, name, is_pkg = next(packages)
                self.__extract_packages(packages)
                self.__extract_modules(loader, name, is_pkg)
            except StopIteration:
                pass
        else:
            raise TypeError("package should be a generator type")

    """ extract modules from the package"""

    def __extract_modules(self, loader, name, is_pkg):

        """ if module found load module and save all attributes in the module found """
        mod = loader.find_module(name).load_module(name)

        """ find the attribute method on each module """
        if hasattr(mod, '__method__'):

            """ register to the blueprint if method attribute found """
            module_router = ModuleRouter(mod).register_route(app=self.application, name=name)

            self.__routers.extend(module_router.routers)
            self.__modules.append(mod)

        else:
            """ prompt not found notification """
            # print('{} has no module attribute method'.format(mod))
            pass

    @property
    def modules(self):
        return self.__modules

    @property
    def routers(self):
        return self.__routers
