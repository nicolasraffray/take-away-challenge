import pytest
from ..lib.twilio import Twilio


@pytest.fixture()
def twilio():
    user_order = {"Tofu": 1, "Fries": 3}
    total = 5
    twilio = Twilio(user_order, total)
    return twilio


@pytest.fixture()
def mockreturn_key():
    return "access_key"


@pytest.fixture()
def mockreturn_sid():
    return 'sid'


class TestTwilio:

    def test_twilio_recieves_orders(self, monkeypatch, twilio, mockreturn_key, mockreturn_sid):
        monkeypatch.setattr(twilio, "api_key", mockreturn_key)
        monkeypatch.setattr(twilio, "account_sid", mockreturn_sid)
        assert twilio.user_order == {"Tofu": 1, "Fries": 3}
        assert twilio.api_key == "access_key"
        assert twilio.account_sid == "sid"
