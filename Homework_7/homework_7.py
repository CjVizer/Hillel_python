"""
Задача - 1
Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
Так же ваш объект должен принимать исключение которое он будет подавлять.
Если флаг об исключении отсутствует, исключение должно быть поднято.
"""
import os
import sys
from time import time_ns
from contextlib import contextmanager


class ToDirectory:
    def __init__(self, directory_path, suppress_exc_flag=None):
        self.directory_path = directory_path
        self.suppress_exc_flag = suppress_exc_flag

    def __enter__(self):
        self.parent_dir = os.getcwd()
        os.chdir(self.directory_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.parent_dir)
        if self.suppress_exc_flag and exc_type == self.suppress_exc_flag:
            print(f'Suppressed exception: {exc_type}, {exc_val}')
            return True


"""
Задача - 2
Описать задачу выше но уже с использованием @contexmanager
"""


@contextmanager
def to_directory(directory_path, suppress_exc_flag=None):
    parent_dir = os.getcwd()
    os.chdir(directory_path)
    try:
        yield
    except Exception as err:
        exc_type, exc_val, exc_tb = sys.exc_info()
        if suppress_exc_flag and exc_type == suppress_exc_flag:
            print(f'Suppressed exception: {exc_type}, {exc_val}')
        else:
            raise
    finally:
        os.chdir(parent_dir)


"""
Задача - 3
Создать менеджер контекста который будет подсчитывать время выполнения вашей функции
"""


class TimeCounter:
    def __enter__(self):
        self.start_time = time_ns()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.lead_time = time_ns() - self.start_time
        print(f'Lead time: {self.lead_time} ns')
