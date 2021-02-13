"""
Текстовый файл содержит записи о телефонах и их владельцах.
Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.
"""


def get_phone_numbers_last_name_startswith(in_file, out_file, *args):
    """
    This function creates a new file with phone numbers of owners
    whose last names begin with the letters specified in args.
    :param in_file: Input file name (input type: str)
    :param out_file: Output file name (input type: str)
    :param args: First letters of surnames (input type: str)
    :return: None
    """
    try:
        with open(in_file, 'r', encoding='utf-8') as db_read:
            with open(out_file, 'w', encoding='utf-8') as db_write:
                for item in db_read:
                    if item.startswith(args):
                        db_write.write(item.split(',')[-1])
    except FileNotFoundError:
        print(f'File with the name "{in_file}" does not exist')


get_phone_numbers_last_name_startswith('db.txt', 'task_db.txt', 'К', 'С')
