class Order():

    def __init__(self, menu):
        self.menu = menu
        self.order = {}

    def make_order(self, order_dict):
        self.order = order_dict
