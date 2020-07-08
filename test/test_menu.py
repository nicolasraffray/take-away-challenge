import pytest
from ..lib.menu import Menu


class TestMenu:

    def test_get_meals(self):
        meals = {"Tofu": 2.50, "Fries": 1.95}
        menu = Menu(meals)
        assert menu.get_meals() == {"Tofu": 2.50, "Fries": 1.95}
