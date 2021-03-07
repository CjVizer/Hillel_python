# Задача4
# Необходимо создать модели работы со складскими запасами товаров и процесса оформления заказа этих товаров.
# Cписок требований:
# +++++ 1) Создайте товар с такими свойствами, как имя(name), подробные сведения(description or details),
# +++++ количество на складе(quantity), доступность(availability), цена(price).
# +++++ 2) Добавить товар на склад.
# +++++ 3) Удалить товар со склада
# +++++ 4) Распечатать остаток товара по его имени
# +++++ 5) Распечатать остаток всех товаров
# +++++ 6) Товар может принадлежать к категории
# +++++ 7) Распечатать список товаров с заданной категорией
# 8) Корзина для покупок, в которой может быть много товаров с общей ценой.
# 9) Добавить товары в корзину (вы не можете добавлять товары, если их нет в наличии)
# 10) Распечатать элементы корзины покупок с ценой и общей суммой
# 11) Оформить заказ и распечатать детали заказа по его номеру
# 12) Позиция заказа, созданная после оформления заказа пользователем.
# Он будет иметь идентификатор заказа(order_id), дату покупки(date_purchased), товары(items), количество(quantity)
# 13) После оформления заказа количество товара уменьшается на количество товаров из заказа.


# Добавить к этой задаче дескриптор для аттрибута цена.
# При назначении цены товара будет автоматически добавлен НДС 20%
# При получении цены товара, цена возврщается уже с учетом НДС
import datetime


class Goods:
    def __init__(
            self,
            name: str,
            description: str = '',
            quantity: int = 0,
            price: float = 0.00
    ):
        self._name = name
        self._description = description
        self._quantity = quantity
        self._availability = True if quantity else False
        self._price = price


class Warehouse:
    def __init__(self):
        self.categories = {}

    def add_goods(self, goods: Goods, category: str = 'No category'):
        if isinstance(goods, Goods):
            if category not in self.categories:
                self.categories[category] = []
            self.categories[category].append(goods)
        else:
            raise ValueError('The goods attribute must be an instance of the "Goods" class')

    def delete_goods(self, name: str):
        result_flag = False
        for category, items in self.categories.items():
            for idx, item in enumerate(items, 0):
                if item._name == name:
                    self.categories[category].pop(idx)
                    result_flag = True
                    print(f'Deleted goods "{name}" from category "{category}"')
        if not result_flag:
            print(f'Product with name "{name}" is out of stock!')

    def print_the_rest_of_the_goods_by_name(self, name: str):
        result_flag = False
        for category, items in self.categories.items():
            for item in items:
                if item._name == name:
                    result_flag = True
                    print(f'{category}: {name} - {item._quantity} pieces')
        if not result_flag:
            print(f'Product with name "{name}" is out of stock!')

    def print_the_rest_of_all_goods(self):
        for category, items in self.categories.items():
            print(category, ':')
            for item in items:
                print(f'\t{item._name}: {item._quantity}')

    def print_goods_by_category(self, category: str):
        if category in self.categories.keys():
            print(f'{category}:')
            for item in self.categories[category]:
                print('\t', end='')
                for item_item in item.__dict__.values():
                    print(f'{item_item}', end=', ')
                print()
        else:
            print('No such category!')


class Basket:
    _order_number = 0

    def __init__(self):
        now = datetime.datetime.now()
        Basket._order_number += 1
        self.order_number = Basket._order_number
        self.order_id = ''.join(map(str, (self.order_number, now.year, now.month,
                                          now.day, now.hour, now.minute, now.second)))
        self.date_purchased = '-'.join(map(str, (now.year, now.month, now.day))) + ' ' + \
                              ':'.join(map(str, (now.hour, now.minute, now.second)))
        self.items = []

    def add_goods(self, name: str, quantity: int):
        pass


def init_goods():
    n1 = Goods('Paper', 'Paper description', 500, 0.2)
    n2 = Goods('Glass', 'Glass description', 2, 208.3)
    n3 = Goods('Stone', 'Stone description', 7, 33.89)
    n4 = Goods('Earphones', 'Earphones description', 32, 135.77)

    f1 = Goods('Banana', 'Banana description', 50, 22.5)
    f2 = Goods('Pineapple', 'Pineapple description', 23, 75.3)
    f3 = Goods('Raspberry', 'Raspberry description', 0, 33.3)
    f4 = Goods('Mango', 'Mango description', 570, 2.25)

    m1 = Goods('STM32F103C8T6', 'STM32F103C8T6 description', 103, 105.02)
    m2 = Goods('STM32F407VET6', 'STM32F407VET6 description', 21, 302.12)
    m3 = Goods('STM32F407VGT6', 'STM32F407VGT6 description', 77, 515.4)
    m4 = Goods('STM32F768XFB4', 'STM32F768XFB4 description', 13, 766.46)

    war = Warehouse()
    war.add_goods(n1)
    war.add_goods(n2)
    war.add_goods(n3)
    war.add_goods(n4)
    war.add_goods(f1, 'Fruits')
    war.add_goods(f2, 'Fruits')
    war.add_goods(f3, 'Fruits')
    war.add_goods(f4, 'Fruits')
    war.add_goods(m1, 'Microcontrollers')
    war.add_goods(m2, 'Microcontrollers')
    war.add_goods(m3, 'Microcontrollers')
    war.add_goods(m4, 'Microcontrollers')


init_goods()

b1 = Basket()
b2 = Basket()
b3 = Basket()
b4 = Basket()
# print(b1.basket_number)
# print(b2.basket_number)
# print(b3.basket_number)
# print(b4.basket_number)
print(b1.order_id)
print(b2.order_id)
print(b3.order_id)
print(b4.order_id)

print(b1.date_purchased)
