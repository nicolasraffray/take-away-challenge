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
