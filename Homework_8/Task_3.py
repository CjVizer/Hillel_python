# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField:
    def __get__(self, instance, owner):
        return instance._number

    def __set__(self, instance, value):
        instance._number = value


class Data:
    number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

print(data_row.number)
print(new_data_row.number)

# assert data_row.number != new_data_row.number
