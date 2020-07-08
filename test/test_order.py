import pytest
from ..lib.order import Order
from ..lib.menu import Menu


@pytest.fixture(scope="module")
def order():
    order = Order(Menu({"Tofu": 2.50, "Fries": 1.95}))
    return order


class TestOrder:

    def test_inherits_menu(self, order):
        assert isinstance(order.menu, Menu)

    def test_user_makes_an_order(self, order):
        ''' Order of 1x Tofu and 2x Fries'''
        order.make_order({"Tofu": 1, "Fries": 2})
        assert order.order == {"Tofu": 1, "Fries": 2}

    def test_get_bill_total(self, order):
        order.make_order({"Tofu": 1, "Fries": 2})
        assert order.get_bill_total() == 6.40
