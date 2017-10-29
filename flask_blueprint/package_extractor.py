import inspect
import pkgutil

from .module_router import ModuleRouter


class PackageExtractor:

    __packages = None
    __modules = []
    __routers = []

    def __init__(self, application, path):
        self.path = path
        self.application = application
        _packages = self.__inspect_packages(packages=pkgutil.walk_packages(path, prefix="", onerror=None))
        self.__extract_packages(packages=_packages)

    @staticmethod
    def __inspect_packages(packages):
        if inspect.isgenerator(packages):
            packages = [package for package in packages]

        if isinstance(packages, (list, set)):
            if len(packages):
                return packages
            else:
                raise ValueError("Package does not have an item.")

    def __extract_packages(self, packages):
        if len(packages):
            self.__extract_modules(package=packages.pop(0)).__extract_packages(packages)

    """ extract modules from the package"""
    def __extract_modules(self, package):
        loader, name, is_pkg = package
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
        return self

    @property
    def modules(self):
        return self.__modules

    @property
    def routers(self):
        return self.__routers
