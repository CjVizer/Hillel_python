import functools
from random import randint


# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.
def decorator_1(func):
    @functools.wraps(func)
    def wrapper():
        result = 100 % func()
        print("We are OK!" if not result else f"Bad news guys, we got {result}")

    return wrapper


@decorator_1
def func_1():
    """Returns random integer from 0 to 100"""
    return randint(0, 100)


# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))
def decorator_2(func):
    @functools.wraps(func)
    def wrapper(arg):
        if isinstance(arg, int):
            print(func(arg))
        elif isinstance(arg, str):
            raise ValueError("string type is not supported")

    return wrapper


@decorator_2
def func_2(arg):
    """Calculates the square of a number"""
    return arg ** 2


# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.
def decorator_3(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            wrapper.cache_calls += 1
            print(f"Used cache with counter = {wrapper.cache_calls}")
            return cache[args]
        else:
            wrapper.function_calls += 1
            cache[args] = func(*args)
            print(f"Function executed with counter = {wrapper.function_calls}, function result = {cache[args]}")
            return cache[args]

    wrapper.function_calls = 0
    wrapper.cache_calls = 0
    return wrapper


@decorator_3
def func_3(name, age):
    """Subtracts from age the number of letters in the name"""
    return age - len(name)
