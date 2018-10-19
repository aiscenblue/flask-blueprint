import inspect


class ModuleRouter:

    __routers = []
    __ignore_names = ["index", "routes"]

    def __init__(self, mod, **kwargs):  # module
        self._module = mod
        if "ignore_names" in kwargs:
            self.__ignore_names.extend(kwargs['ignore_names'])
        if self._is_valid_module():
            self.model_add_router()

    def model_add_router(self):
        if hasattr(self._module, '__routes__') and len(self._module.__routes__):
            route_type, route_data = self._routing_type(route=self._module.__routes__.pop(0))
            if route_type == 'cls':
                """ If it's a class it needs to extract the methods by function names
                    magic functions are excluded
                """
                route_name, slug, cls = route_data
                self.class_member_route(route=route_data, members=self.get_cls_fn_members(cls))

            elif route_type == 'fn':
                route_name, slug, fn, methods = route_data
                self.__routers.append(route_data)
                self._module.__method__.add_url_rule(
                    rule=slug,
                    endpoint=fn.__name__,
                    view_func=fn,
                    methods=methods)
            self.model_add_router()

    def _is_valid_module(self):
        return hasattr(self._module, '__routes__') or hasattr(self._module, '__method__')

    @staticmethod
    def _routing_type(route):
        __type = None
        if isinstance(route, tuple):
            if len(route) == 3 and inspect.isclass(route[2]):
                __type = 'cls'
            elif len(route) == 4 and inspect.isfunction(route[2]):
                if isinstance(route[3], (list, tuple, set)):
                    __type = 'fn'
                else:
                    raise TypeError("methods must be a list.")
            else:
                raise TypeError("Invalid route syntax.")
        return __type, route

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

    @staticmethod
    def get_cls_fn_members(cls):
        return [member for member in inspect.getmembers(cls, predicate=inspect.isfunction)]

    def class_member_route(self, route, members):
        if isinstance(members, (list, set)):
            if len(members):
                (fn_name, fn_object) = members.pop(0)
                route_name, slug, cls = route
                if inspect.isfunction(fn_object):

                    _methods = self.get_http_methods([fn_name])

                    self._module.__method__.add_url_rule(
                        rule=slug,
                        endpoint=fn_name,
                        view_func=fn_object,
                        methods=_methods)
                    self.__routers.append((slug, fn_name, fn_object, _methods))
                else:
                    raise KeyError("Member is not a function.")
                self.class_member_route(route, members)
        else:
            raise TypeError("members must be a list.")

    def register_route(self, app, name):
        app.register_blueprint(self._module.__method__, url_prefix=self.blueprint_name(name))
        return self

    def ignore_default_names(self, name):
        for ignore_name in list(set(self.__ignore_names)):
            if ignore_name in name:
                name = str(name).replace(ignore_name, "")
        return name

    def blueprint_name(self, name):
        """ set index automatically as home page """
        return self.blueprint_name_to_url(self.ignore_default_names(name))

    @staticmethod
    def blueprint_name_to_url(name):
        """ remove the last . in the string it it ends with a .
            for the url structure must follow the flask routing format
            it should be /model/method instead of /model/method/
        """
        if name[-1:] == ".":
            name = name[:-1]
        name = str(name).replace(".", "/")
        return name

    @property
    def routers(self):
        return self.__routers
