import pytest
from Homework_11.src.task_4 import Goods
from Homework_11.src.task_4 import Warehouse
from Homework_11.src.task_4 import Cart
from Homework_11.src.task_4 import Orders


@pytest.fixture(scope="function")
def goods_obj():
    return Goods('Apple', 'Fruit from the tree', 20.0)


@pytest.fixture(scope="function")
def warehouse_obj():
    return Warehouse()


@pytest.fixture(scope="function")
def cart_obj():
    return Cart()


@pytest.fixture(scope="function")
def orders_obj():
    return Orders()
