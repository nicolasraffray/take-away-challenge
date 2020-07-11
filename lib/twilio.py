from .config import api_key, account_sid
from twilio.rest import Client

# print(config.API_KEY)


class Twilio:

    def __init__(self, order, total):
        self.user_order = order
        self.order_total = total
        self.api_key = api_key
        self.account_sid = account_sid

    def send_message(self):
        client = Client(self.account_sid, self.api_key)
        message = client.messages.create(
            to="+447533828082",
            from_="+441212855168",
            body="Hello from Python!")
        message.sid
