class Order():

    def __init__(self, menu):
        self.menu = menu
        self.order = {}

    def make_order(self, order_dict):
        self.order = order_dict

    def get_bill_total(self, check_menu=None):
        if check_menu:
            meals = check_menu.get_meals()
        else:
            meals = self.menu.get_meals()
        bill = 0
        for meal in self.order:
            bill += meals[meal] * self.order[meal]
        return bill

    def check_order(self, menu):
        total = self.get_bill_total()
        check_total = self.get_bill_total(menu)
        if total == check_total:
            return "Total is correct"
        else:
            return "Total is incorrect for the menu being checked against"
