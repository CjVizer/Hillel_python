"""
Получить файл, в котором текст выровнен по правому краю путем равномерного добавления пробелов.
"""


def align_right(in_file, out_file):
    """
    This function right-aligns text in a file
    :param in_file: Input file name (input type: str)
    :param out_file: Output file name (input type: str)
    :return: None
    """
    try:
        with open(in_file, 'r', encoding='utf-8') as input_file:
            with open(out_file, 'w', encoding='utf-8') as output_file:
                max_length = 0
                for line in input_file:
                    line_length = len(line)
                    if line_length > max_length:
                        max_length = line_length

                input_file.seek(0)
                for line in input_file:
                    output_file.write(line.rjust(max_length))
    except FileNotFoundError:
        print(f'File with the name "{in_file}" does not exist')


align_right('poem.txt', 'poem_rjust.txt')
