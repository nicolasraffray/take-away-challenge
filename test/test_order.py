import pytest
from ..lib.order import Order
from ..lib.menu import Menu


class TestOrder:

    def test_inherits_menu(self):
        order = Order(Menu({"Tofu": 2.50, "Fries": 1.95}))
        assert isinstance(order.menu, Menu)
