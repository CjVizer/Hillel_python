# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```
from functools import wraps
from time import sleep


def coroutine(func):
    """Decorator for initialization coroutine"""

    @wraps(func)
    def init(*args, **kwargs):
        function = func(*args, **kwargs)
        next(function)
        return function

    return init
    pass


@coroutine
def grep(*args):
    pattern, printer_func = args
    while True:
        line = yield
        if pattern in line:
            printer_func.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line.strip('\n'))


@coroutine
def dispenser(*args):
    while True:
        line = yield
        for grep_cr in args[0]:
            grep_cr.send(line)


def follow(*args):
    file, disp = args
    file.seek(0, 2)
    while True:
        line = file.readline()
        if line:
            disp.send(line)
        sleep(0.5)


# ```
#
# Каждый grep следит за определенной сигнатурой
#
# Как это будет работать:
#
# ```
f_open = open('log.txt')  # подключаемся к файлу
follow(f_open,
       # делегируем ивенты
       dispenser([
           grep('python', printer()),  # отслеживаем
           grep('is', printer()),  # заданные
           grep('great', printer()),  # сигнатуры
       ])
       )
# ```
# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть
#
# Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.
#
# Если все плохо - план Б лекция Дэвида Бизли
# [warning] решение там тоже есть :)
# https://www.dabeaz.com/coroutines/Coroutines.pdf
