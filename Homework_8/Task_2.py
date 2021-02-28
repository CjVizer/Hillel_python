# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):

    def __call__(cls, *args, **kwargs):
        # your code here
        pass


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)
