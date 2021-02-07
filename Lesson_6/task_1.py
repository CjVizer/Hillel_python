import time
from functools import wraps


def time_log(func):
    @wraps(func)
    def wrapper(*args):
        start_time = time.time()
        func_result = func(*args)
        time_result = time.time() - start_time
        result_string = (f'Function result: {func_result}\n'
                         f'Function name: {func.__name__}\n'
                         f'Function time: {time_result}')
        print(result_string)
        with open("log.txt", "w") as log:
            log.write(result_string)

    return wrapper


@time_log
def list_creator(range_number):
    my_list = []
    for number in range(0, range_number):
        my_list.append(number)
    return my_list


list_creator(100000)
