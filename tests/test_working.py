import pytest
from working import convert


def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_noon_midnight_and_overnight():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:45 PM") == "00:30 to 12:45"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"


def test_invalid_times():
    invalid_inputs = [
        "13:00 PM to 5:00 PM",
        "9:60 AM to 5:00 PM",
        "12:60 AM to 5:00 PM",
        "0 AM to 5 PM",
        "9:00 XM to 5:00 PM",
        "9 AM - 5 PM",
        "9:00AM to 5:00PM",
        "9:00 AM to 5:00 PM extra",
        "9:00 to 5:00 PM",
    ]

    for value in invalid_inputs:
        with pytest.raises(ValueError):
            convert(value)