# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить
import re

pattern = re.compile("[A-Za-z0-9]+@[a-z.]+")


class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance._email

    def __set__(self, instance, value):
        if re.findall(pattern, value):
            instance._email = value
        else:
            raise ValueError('Invalid email format')


class MyClass:
    def __init__(self):
        self._email = ''

    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"

my_class.email = "novalidemail"
# Raised Exception
