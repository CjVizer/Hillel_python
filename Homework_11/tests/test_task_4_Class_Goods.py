import pytest


# Nds class testing
def test_goods_nds_wrong_type_of_data(goods_obj):
    with pytest.raises(TypeError):
        goods_obj.price = []


def test_goods_nds_get(goods_obj):
    assert goods_obj.price == round(20.0 + 20.0 * 0.2, 2)


def test_goods_nds_set(goods_obj):
    goods_obj.price = 10
    assert goods_obj.price == round(10 + 10 * 0.2, 2)


# Setters and getters testing
def test_goods_name_setter_getter(goods_obj):
    goods_obj.name = 'Test name'
    assert goods_obj.name == 'Test name'


def test_goods_description_setter_getter(goods_obj):
    goods_obj.description = 'Test description'
    assert goods_obj.description == 'Test description'


def test_goods_quantity_setter_getter(goods_obj):
    goods_obj.quantity = 10
    assert goods_obj.quantity == 10


# Availability logic testing
def test_goods_availability_false_state(goods_obj):
    goods_obj.quantity = 0
    assert not goods_obj._availability


def test_goods_availability_true_state(goods_obj):
    goods_obj.quantity = 1
    assert goods_obj._availability


# String representation testing
def test_goods_str_representation(goods_obj):
    result = goods_obj.__str__()
    reference = '\tApple:\n' \
                '\t\tDescription: Fruit from the tree\n' \
                '\t\tQuantity: 0\n' \
                '\t\tAvailability: False\n' \
                '\t\tPrice: 24.0 UAH'
    assert reference == result
