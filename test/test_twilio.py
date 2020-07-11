import pytest
from unittest import mock, TestCase
from ..lib.twilio import Twilio
from twilio.rest import Client


@pytest.fixture()
def twilio():
    user_order = {"Tofu": 1, "Fries": 3}
    total = 5
    twilio = Twilio(user_order, total)
    twilio = Twilio({"Tofu": 1, "Fries": 3}, 5)
    twilio.api_key = "access_key"
    twilio.account_sid = "sid"
    return twilio


@pytest.fixture()
def mockreturn_key():
    return "access_key"


@pytest.fixture()
def mockreturn_sid():
    return 'sid'


class TestTwilio():

    def test_twilio_recieves_orders(self, monkeypatch, twilio):
        # monkeypatch.setattr(twilio, "api_key", mockreturn_key)
        # monkeypatch.setattr(twilio, "account_sid", mockreturn_sid)
        assert twilio.user_order == {"Tofu": 1, "Fries": 3}
        assert twilio.api_key == "access_key"
        assert twilio.account_sid == "sid"
