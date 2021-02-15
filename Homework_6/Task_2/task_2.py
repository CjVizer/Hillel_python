"""
Задача-2

У вас несколько JSON файлов. В каждом из этих файлов есть произвольная структура данных.
Вам необходимо написать класс который будет описывать работу с этими файлами,
а именно:
1) Запись в файл
2) Чтение из файла
3) Объединение данных из файлов в новый файл
4) Получить путь относительный путь к файлу
5) Получить абсолютный путь к файлу
"""
import json
import os


class JsonHandler:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__combined_file_data = {}

    def __write_json(self, output_file_name):
        output_data = json.dumps(self.__combined_file_data, sort_keys=True, indent=4)
        with open(output_file_name, 'w') as output_file:
            output_file.write(output_data)

    def read_json(self, file_path=None):
        if not file_path:
            file_path = self.__file_name
        try:
            with open(file_path, 'r') as file:
                file_data = file.read()
            return json.loads(file_data)
        except FileNotFoundError:
            print(f'File with the name "{self.__file_name}" does not exist')

    def combine_json(self, output_file_name, *args):
        self.__combined_file_data.clear()
        self.__combined_file_data['Json1'] = self.read_json()
        for count, file_path in enumerate(args, 2):
            self.__combined_file_data[f'Json{count}'] = self.read_json(file_path)
        self.__write_json(output_file_name)

    def get_relative_path(self):
        return os.path.relpath(os.path.abspath(self.__file_name), __file__)

    def get_absolute_path(self):
        return os.path.abspath(self.__file_name)
