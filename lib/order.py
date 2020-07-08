class Order():

    def __init__(self, menu):
        self.menu = menu
        self.order = {}

    def make_order(self, order_dict):
        self.order = order_dict

    def get_bill_total(self):
        meals = self.menu.get_meals()
        bill = 0
        for meal in self.order:
            bill += meals[meal] * self.order[meal]
        return bill
