# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)
