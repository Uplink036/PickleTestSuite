# https://medium.com/@ramanbazhanau/mastering-advanced-oop-concepts-in-python-advanced-class-features-a8790fa2b5a2

class ProtectedAttributes:
    def __init__(self):
        self._protected = "This is protected"

    def __getattr__(self, name):
        if name == "secret":
            raise AttributeError("Access Denied")
        return self.__dict__.get(name, f"{name} not found")

    def __setattr__(self, name, value):
        if name == "secret":
            raise AttributeError("Cannot modify secret")
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name == "secret":
            raise AttributeError("Cannot delete secret")
        del self.__dict__[name]
