"""
Реализовать объект FibonacciIter.

пример использования
for i in FibonacciIter():
     print(i)

     if i > 100:
         break
"""


class FibonacciIter:
    def __init__(self):
        self.fib1, self.fib2 = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        res = self.fib1
        self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
        return res


for i in FibonacciIter():
    print(i)
    if i > 100:
        break

"""
2) Реализовать тот же пример но уже через функцию генератор. 
пример использования
"""


def fibonacci():
    fib1, fib2 = 0, 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


for i in fibonacci():
    print(i)
    if i > 100:
        break

"""
3) Реализовать генератор count(start_val=0, step_val=1). 
Вы должны будете увеличивать коунтер на величину указанную в step_val при каждом вызове next()
"""


def count(start_val=0, step_val=1):
    while True:
        yield start_val
        start_val += step_val


counter = count(0, 2)
print(next(counter))
print(next(counter))
print(next(counter))

"""
4) Дополнить реализацию задачи 3 и сделать ее корутиной, 
тем самым позволяя изменять start_val уже после инициализации генератора.
counter.send(200)
"""


def count(start_val=0, step_val=1):
    while True:
        new_start_val = yield start_val
        if isinstance(new_start_val, int):
            start_val = new_start_val
        else:
            start_val += step_val


counter = count(0, 5)
for i in counter:
    print(i)

    if i == 10:
        print(counter.send(200))

    if i >= 300:
        break
