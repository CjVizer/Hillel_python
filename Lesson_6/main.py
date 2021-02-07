import functools


def my_new_decorator_with_params(decorator_params):
    def my_new_decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            print(f'Before msg = {decorator_params}')
            func(args)

        return wrapper

    return my_new_decorator


@my_new_decorator_with_params('Hello world')
def my_func(a):
    """This is description of my function"""
    print(a)
    return a


my_func(100)
print(my_func.__name__, my_func.__doc__, my_func.__module__)
