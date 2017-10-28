import inspect
import pkgutil

from module_router import ModuleRouter


class PackageExtractor:

    __packages = None

    def __init__(self, application, path):
        self.path = path
        self.application = application
        _packages = self.__inspect_packages(packages=pkgutil.walk_packages(path, prefix="", onerror=None))
        self.extract_packages(packages=_packages)

    @staticmethod
    def __inspect_packages(packages):
        if inspect.isgenerator(packages):
            packages = [package for package in packages]

        if isinstance(packages, (list, set)):
            if len(packages):
                return packages
            else:
                raise ValueError("Package does not have an item.")

    def extract_packages(self, packages):
        if len(packages):
            loader, name, is_pkg = packages.pop(0)
            """ if module found load module and save all attributes in the module found """
            mod = loader.find_module(name).load_module(name)

            """ find the attribute method on each module """
            if hasattr(mod, '__method__'):
                module_router = ModuleRouter(mod)

                """ register to the blueprint if method attribute found """
                module_router.register_route(app=self.application, name=name)

            else:
                """ prompt not found notification """
                # print('{} has no module attribute method'.format(mod))
                pass
            self.extract_packages(packages)

