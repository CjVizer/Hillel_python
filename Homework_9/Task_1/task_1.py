# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем

def file_line_reader(path):
    file_data = None
    unique = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            file_data = file.readlines()
    except FileNotFoundError:
        print(f'File "{path}" does not exist')

    while file_data:
        line = file_data.pop(0)
        if line not in unique:
            unique.append(line)
            print(line, end='')
        yield


gen = file_line_reader('file.txt')

# Tests
# print(type(gen))
# for lines in gen:
#     pass
