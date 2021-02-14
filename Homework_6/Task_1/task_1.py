"""
Задача-1

У вас есть список(list) IP адрессов. Вам необходимо создать
класс который будет иметь методы:
1) Получить список IP адресов
2) Получить список IP адресов в развернутом виде (10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов (10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов (10.11.12.13 -> 13)
"""
from random import randint


class IpHolder:
    def __init__(self, ip_list):
        self.__ip_list = ip_list

    def get_ips(self):
        return self.__ip_list

    def get_deployed_ips(self):
        return ['.'.join(octet for octet in ip_address.split('.')[::-1]) for ip_address in self.__ip_list]

    def get_ips_without_first_octet(self):
        return ['.'.join(octet for octet in ip_address.split('.')[1:]) for ip_address in self.__ip_list]

    def get_ips_last_octets(self):
        return [ip_address.split('.')[-1] for ip_address in self.__ip_list]


# Tests
ip = ['.'.join(str(randint(0, 255)) for _ in range(4)) for _ in range(300)]

ip_holder = IpHolder(ip)
print(ip_holder.get_ips())
print(ip_holder.get_deployed_ips())
print(ip_holder.get_ips_without_first_octet())
print(ip_holder.get_ips_last_octets())
