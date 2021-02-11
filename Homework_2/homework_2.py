from random import choice

# 1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
result_1 = {i: i * i for i in keys}

# 2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
result_2 = [i for i in range(0, 100) if i % 2 == 0]

# 3) Заменить в произвольной строке согласные буквы на гласные.
my_string = 'Basic data structures 765%&=='
vowels = "aeiouAEIOU"
result_3 = ''.join(letter if letter in vowels or not letter.isalpha() else choice(vowels) for letter in my_string)

# 4) Дан массив чисел.
my_list4 = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# 4.1) убрать из него повторяющиеся элементы
result_4 = list(set(my_list4))
# 4.2) вывести 3 наибольших числа из исходного массива
print(sorted(my_list4)[-3:])
# 4.3) вывести индекс минимального элемента массива
print(my_list4.index(min(my_list4)))
# 4.4) вывести исходный массив в обратном порядке
print(my_list4[::-1])

# 5) Найти общие ключи в двух словарях:
dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}
result_5 = dict_one.keys() & dict_two.keys()

# 6)Дан массив из словарей
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 6.1) отсортировать массив из словарей по значению ключа 'age'
result_6_1 = sorted(data, key=lambda i: i['age'])
# 6.2) сгруппировать данные по значению ключа 'city'
# вывод должен быть такого вида :
# result = {
#     'Kiev': [
#         {'name': 'Viktor', 'age': 30},
#         {'name': 'Andrey', 'age': 34}],
#
#     'Dnepr': [{'name': 'Maksim', 'age': 20},
#               {'name': 'Artem', 'age': 50}],
#     'Lviv': [{'name': 'Vladimir', 'age': 32},
#              {'name': 'Dmitriy', 'age': 21}]
# }
result_6_2 = {i['city']: [] for i in data}
for i in data:
    result_6_2[i['city']].append({'name': i['name'], 'age': i['age']})


# =======================================================
# 7) У вас есть последовательность строк.
# Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:

# def most_frequent(list_var):
#     # your code is here
#     return


# most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'


def most_frequent(list_var):
    result_7 = ''
    for i in list_var:
        if list_var.count(i) > list_var.count(result_7):
            result_7 = i
    return result_7


most_frequent(['a', 'a', 'bi', 'bi', 'bi'])

# =======================================================
# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.
num = 123405
result_8 = 1
for i in str(num):
    if int(i):
        result_8 *= int(i)


# =======================================================
# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.
def some_function(array, n):
    return array[n] ** n if n < len(array) else -1


some_function([0, 1, 2, 3, 4, 5, 6, 7, 8], 3)

# =======================================================
# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.
my_string_10 = 'hello 1 one two three 15 world'


def my_func(text):
    counter = 0
    for i in my_string_10.split():
        if i.isalpha():
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0
    return False


my_func(my_string_10)