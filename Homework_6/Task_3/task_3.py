"""
Задача-3

Создайте класс который будет хранить параметры для подключения к физическому юниту(например switch).
В своем списке атрибутов он должен иметь минимальный набор (unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и сеттеров(@property).
У вас должна быть возможность получения и назначения этих атрибутов в классе.
"""


class Unit:
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self.__unit_name = unit_name
        self.__mac_address = mac_address
        self.__ip_address = ip_address
        self.__login = login
        self.__password = password

    @property
    def unit_name(self):
        return self.__unit_name

    @unit_name.setter
    def unit_name(self, new_name):
        self.__unit_name = new_name

    @property
    def mac_address(self):
        return self.__mac_address

    @mac_address.setter
    def mac_address(self, new_mac_address):
        self.__mac_address = new_mac_address

    @property
    def ip_address(self):
        return self.__ip_address

    @ip_address.setter
    def ip_address(self, new_ip_address):
        self.__ip_address = new_ip_address

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, new_login):
        self.__login = new_login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password
