"""
Создать объект менеджера контекста который будет переходить по заданному юрл,
при этом отловить requests.exceptions.ConnectionError.
в теле менеджера записать html файл и закрыть его
"""

import requests


class RequestException:
    def __init__(self, url, exc=None):
        self._url = url
        self._exc = exc or Exception

    def __enter__(self):
        try:
            result = requests.get(self._url)
        except self._exc:
            raise self._exc('THIS IS ERROR!!!')
        return str(result.content)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Exception {exc_type}, {exc_val}')


with RequestException('http://www.google.co2m', requests.exceptions.ConnectionError) as page:
    with open('test.html', 'w') as file:
        file.write(page)
