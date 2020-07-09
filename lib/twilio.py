from .config import api_key, account_sid

# print(config.API_KEY)


class Twilio:

    def __init__(self, order, total):
        self.user_order = order
        self.order_total = total
        self.api_key = api_key
        self.account_sid = account_sid
