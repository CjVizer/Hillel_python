def test_orders_init(orders_obj):
    assert (isinstance(orders_obj.order_number, int) and
            isinstance(orders_obj.orders, dict) and
            not orders_obj.order_number and
            not orders_obj.orders)


def test_orders_print_order_info_wrong_order_number(orders_obj, capsys):
    orders_obj.print_order_info(1)
    captured = capsys.readouterr()
    assert captured.out == 'Order with number "1" not found\n'


def test_orders_place_an_order_wrong_type_of_data(orders_obj, capsys):
    orders_obj.place_an_order(123)
    captured = capsys.readouterr()
    assert captured.out == '"Order" must correspond to the "Cart" class\n'
