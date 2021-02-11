from functools import wraps
from time import time, sleep


# LRU (least recently used) — это алгоритм, при котором вытесняются значения, которые дольше всего не запрашивались.
# Соответственно, необходимо хранить время последнего запроса к значению. И как только число закэшированных значений
# превосходит N необходимо вытеснить из кеша значение, которое дольше всего не запрашивалось.
#
#
# Задача - 1
# Создать декоратор lru_cache(подобный тому который реализован в Python).
def my_lru_cache(max_size=8):
    def my_lru_cache_wrapper(func):
        cache = {}  # Dictionary to store the cache {attributes: function result}
        time_of_the_last_call = {}  # Dictionary to store the time of the last call from cache {attributes: time}

        @wraps(func)
        def wrapper(*args):
            if args in cache:
                time_of_the_last_call[args] = time()
                wrapper.cache_called += 1
                return cache[args]
            else:
                # If there is no free space left in the cache
                if len(cache) >= max_size:
                    # We are looking for the smallest time value and write attributes from this time to pop_key
                    pop_key = sorted(time_of_the_last_call.items(), key=lambda value: value[1])[0][0]
                    # Then remove the key-value from the cache
                    cache.pop(pop_key)
                    # and remove the key-value from the time holder
                    time_of_the_last_call.pop(pop_key)
                time_of_the_last_call[args] = time()
                cache[args] = func(*args)
                wrapper.function_called += 1
                return cache[args]

        # Задача-2
        # Ваш lru_cache декоратор должен иметь служебный метод
        # cache_info  - статистика использования вашего кеша(например: сколько раз вычислялась ваша функция,
        # а сколько раз значение было взято из кеша, сколько места свободно в кеше)
        def cache_info(show_cache=False):
            if show_cache:
                if cache:
                    for key, value in cache.items():
                        print(f'Key: {key}, Value: {value}, Time of last call: {time_of_the_last_call[key]}')
                else:
                    print('Cache empty.')
            print(f'Cache total space: {max_size}')
            print(f'Cache free space: {max_size - len(cache)}')
            print(f'Cache used space: {len(cache)}')
            print(f'Function called: {wrapper.function_called} times')
            print(f'Cache called: {wrapper.cache_called} times')
            print()

        # Задача-3
        # Ваш lru_cache декоратор должен иметь служебный метод
        # cache_clear - очищает кеш
        def cache_clear():
            cache.clear()
            time_of_the_last_call.clear()
            wrapper.cache_called = 0
            wrapper.function_called = 0

        wrapper.cache_called = 0
        wrapper.function_called = 0
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear
        return wrapper

    return my_lru_cache_wrapper


@my_lru_cache(20)
def sum_of_numbers(number1, number2):
    """Calculates the sum of numbers"""
    return number1 + number2


for i in range(12):
    sum_of_numbers(50, i)
    sleep(0.2)
    if i == 5:
        sum_of_numbers(50, 0)
    if i == 6:
        sum_of_numbers(50, 3)

sum_of_numbers.cache_info(show_cache=True)
sum_of_numbers.cache_clear()
sum_of_numbers.cache_info(show_cache=True)
