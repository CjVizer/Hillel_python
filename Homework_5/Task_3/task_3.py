"""
Получить файл, в котором текст выровнен по правому краю путем равномерного добавления пробелов.
"""

with open('poem.txt', 'r', encoding='utf-8') as poem:
    with open('poem_rjust.txt', 'w', encoding='utf-8') as poem_rjust:
        max_length = 0
        for line in poem:
            line_length = len(line)
            if line_length > max_length:
                max_length = line_length

        poem.seek(0)
        for line in poem:
            poem_rjust.write(line.rjust(max_length))
