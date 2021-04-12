def test_warehouse_init(warehouse_obj):
    assert isinstance(warehouse_obj._categories, dict) and not warehouse_obj._categories


# add_goods method testing
def test_warehouse_add_goods_wrong_type_of_data(warehouse_obj, capsys):
    warehouse_obj.add_goods(123)
    captured = capsys.readouterr()
    assert captured.out == '"goods" must correspond to the "Goods" class\n'


def test_warehouse_add_goods_creating_new_category(warehouse_obj, goods_obj):
    warehouse_obj.add_goods(goods_obj)
    assert 'No category' in warehouse_obj._categories


def test_warehouse_add_goods_creating_two_categories(warehouse_obj, goods_obj):
    warehouse_obj.add_goods(goods_obj)
    warehouse_obj.add_goods(goods_obj, category='Test category')
    assert ['No category', 'Test category'] == list(warehouse_obj._categories.keys())


def test_warehouse_add_goods_if_product_not_in_warehouse(warehouse_obj, goods_obj):
    warehouse_obj.add_goods(goods_obj)
    assert goods_obj in warehouse_obj._categories['No category']


def test_warehouse_add_goods_updating_quantity_if_product_not_in_warehouse(warehouse_obj, goods_obj):
    warehouse_obj.add_goods(goods_obj, 5)
    assert goods_obj._quantity == 5


def test_warehouse_add_goods_updating_quantity_if_product_already_was_in_warehouse(warehouse_obj, goods_obj):
    warehouse_obj.add_goods(goods_obj, 5)
    warehouse_obj.add_goods(goods_obj, 5)
    assert goods_obj._quantity == 10


# delete_goods method testing
def test_warehouse_delete_goods_wrong_type_of_data(warehouse_obj, capsys):
    warehouse_obj.delete_goods(123)
    captured = capsys.readouterr()
    assert captured.out == '"goods" must correspond to the "Goods" class\n'


def test_warehouse_delete_goods_try_to_delete_goods(warehouse_obj, goods_obj):
    warehouse_obj.add_goods(goods_obj, 5)
    warehouse_obj.delete_goods(goods_obj)
    assert goods_obj not in warehouse_obj._categories['No category']


def test_warehouse_delete_goods_message_after_deleting_goods(warehouse_obj, goods_obj, capsys):
    warehouse_obj.add_goods(goods_obj, 5)
    warehouse_obj.delete_goods(goods_obj)
    captured = capsys.readouterr()
    assert captured.out == 'Deleted "Apple" from "No category" category\n'
