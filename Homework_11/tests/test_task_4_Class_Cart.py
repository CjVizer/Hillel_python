def test_cart_init(cart_obj):
    assert (isinstance(cart_obj._goods, dict) and
            isinstance(cart_obj._total_price, float) and
            not cart_obj._goods and
            not cart_obj._total_price)


# add_goods method testing
def test_cart_add_goods_wrong_type_of_data(cart_obj, capsys):
    cart_obj.add_goods(123)
    captured = capsys.readouterr()
    assert captured.out == '"goods" must correspond to the "Goods" class\n'


def test_cart_add_goods_not_enough_goods(cart_obj, goods_obj, capsys):
    cart_obj.add_goods(goods_obj)
    captured = capsys.readouterr()
    assert captured.out == f'There is not enough product named "{goods_obj.name}" in stock\n'


def test_cart_add_goods_appending_new_item(cart_obj, goods_obj):
    goods_obj._quantity = 1
    cart_obj.add_goods(goods_obj)
    assert goods_obj in cart_obj._goods and cart_obj._goods[goods_obj] == 1


def test_cart_add_goods_updating_total_price(cart_obj, goods_obj):
    goods_obj._quantity = 1
    cart_obj.add_goods(goods_obj)
    assert cart_obj._total_price == goods_obj.price


def test_cart_print_basket_cart_ie_empty_msg(cart_obj, capsys):
    cart_obj.print_basket_items()
    captured = capsys.readouterr()
    assert captured.out == 'Cart is empty\nTotal price: 0.0 UAH\n'


def test_cart_get_items(warehouse_obj, cart_obj, goods_obj):
    warehouse_obj.add_goods(goods_obj, 1)
    cart_obj.add_goods(goods_obj, 1)
    assert cart_obj.get_items() == {goods_obj: 1}
