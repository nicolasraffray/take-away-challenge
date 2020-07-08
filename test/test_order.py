import pytest
from ..lib.order import Order
from ..lib.menu import Menu


@pytest.fixture()
def order():
    order = Order(Menu({"Tofu": 2.50, "Fries": 1.95}))
    return order


def test_inherits_menu(order):
    assert isinstance(order.menu, Menu)
