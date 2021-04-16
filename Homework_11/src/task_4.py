from datetime import datetime


class Goods:
    class Nds:
        def __get__(self, instance, owner):
            return instance._price

        def __set__(self, instance, value):
            instance._price = round(value + value * 0.2, 2)

    def __init__(self, name: str, description: str = '', price: float = 0.00):
        self._name = name
        self._description = description
        self._quantity = 0
        self._availability = False
        self._price = round(price + price * 0.2, 2)

    def __str__(self):
        return f'\t{self._name}:\n' \
               f'\t\tDescription: {self._description}\n' \
               f'\t\tQuantity: {self._quantity}\n' \
               f'\t\tAvailability: {self._availability}\n' \
               f'\t\tPrice: {self._price} UAH'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity
        self._availability = True if self._quantity else False

    @property
    def availability(self):
        return self._availability

    price = Nds()


class Warehouse:
    def __init__(self):
        self._categories = {}

    def add_goods(self, goods: Goods, quantity: int = 0, category: str = 'No category'):
        if isinstance(goods, Goods):
            if category not in self._categories:
                self._categories[category] = []
            if goods in self._categories[category]:
                goods.quantity = goods.quantity + quantity
            else:
                self._categories[category].append(goods)
                goods.quantity = quantity
        else:
            print('"goods" must correspond to the "Goods" class')

    def delete_goods(self, goods: Goods):
        if isinstance(goods, Goods):
            for category, items in self._categories.items():
                if goods in items:
                    self._categories[category].pop(self._categories[category].index(goods))
                    print(f'Deleted "{goods.name}" from "{category}" category')
        else:
            print('"goods" must correspond to the "Goods" class')

    def print_the_rest_of_the_goods(self):
        for category, items in self._categories.items():
            print(f'Category: "{category}"')
            for item in items:
                print(item)
            print()

    def print_the_rest_of_the_goods_by_name(self, name: str):
        goods_flag = False
        for category, items in self._categories.items():
            for item in items:
                if item.name == name:
                    goods_flag = True
                    print(f'{name}: {item.quantity} pieces')
        if not goods_flag:
            print(f'Item named "{name}" is out of stock')

    def print_the_rest_of_the_goods_by_category(self, category: str):
        if category in self._categories:
            print(f'{category}:')
            for item in self._categories[category]:
                print(item)
        else:
            print(f'Categories named "{category}" do not exist')


class Cart:
    def __init__(self):
        self._goods = {}
        self._total_price = 0.0

    def add_goods(self, goods: Goods, quantity: int = 1):
        if isinstance(goods, Goods):
            if goods.quantity >= quantity:
                self._goods[goods] = quantity
                self._total_price += round(goods.price * quantity, 2)
            else:
                print(f'There is not enough product named "{goods.name}" in stock')
        else:
            print('"goods" must correspond to the "Goods" class')

    def print_basket_items(self):
        result = 'Goods in cart:\n' if self._goods else 'Cart is empty\n'
        for goods, quantity in self._goods.items():
            result += f'\t{goods.name}: {quantity} pieces X {goods.price} UAH = {round(goods.price * quantity, 2)} UAH\n'
        result += f'Total price: {self._total_price} UAH'
        print(result)

    def get_items(self):
        return self._goods


class Orders:
    def __init__(self):
        self.order_number = 0
        self.orders = {}

    def print_order_info(self, order_number: int):
        result = ''
        if order_number in self.orders:
            result += f'Order id: {order_number} \n' \
                      f'Purchase date: {self.orders[order_number]["date_purchased"]}\n' \
                      f'Items:\n'
            for item in self.orders[order_number]['items']:
                result += f'\t{item.name} - {self.orders[order_number]["items"][item]} pieces\n'
            print(result)
        else:
            print(f'Order with number "{order_number}" not found')

    def place_an_order(self, order: Cart):
        if isinstance(order, Cart):
            self.orders[self.order_number] = {'date_purchased': '{:%d.%m.%Y %H:%M}'.format(datetime.now()),
                                              'items': order.get_items()}
            print(f'Order is processed!')
            self.print_order_info(self.order_number)
            for item, value in self.orders[self.order_number]['items'].items():
                item.quantity -= value
            self.order_number += 1
        else:
            print('"Order" must correspond to the "Cart" class')
