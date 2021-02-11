"""
Текстовый файл содержит записи о телефонах и их владельцах.
Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.
"""

with open('db.txt', 'r', encoding='utf-8') as db_read:
    with open('task_db.txt', 'w', encoding='utf-8') as db_write:
        for item in db_read:
            if item.startswith(('К', 'С')):
                db_write.write(item.split(',')[-1])
