# Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и
# обработку ошибки GeneratorExit.
#
# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция )
# в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.
from functools import wraps


def coroutine_initializer(func):
    """Coroutine initializer"""

    @wraps(func)
    def init(*args, **kwargs):
        function = func(*args, **kwargs)
        next(function)
        return function

    return init


@coroutine_initializer
def coroutine_1():
    cr = coroutine_2()
    while True:
        try:
            elem = yield
            print(f'CR_1 take element {elem}')
            cr.send(elem)
        except GeneratorExit:
            print('"Coroutine 1" DONE!')
            raise


@coroutine_initializer
def coroutine_2():
    while True:
        try:
            elem = yield
            print(f'CR_2 take element {elem}')
        except GeneratorExit:
            print('"Coroutine 2" DONE!')
            raise


def source():
    cr = coroutine_1()
    elements = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    for elem in elements:
        cr.send(elem)


source()
