import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("0/4") == 0
    assert convert("1/1") == 100


def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("3")

    with pytest.raises(ValueError):
        convert("1/2/3")

    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        convert("4/3")


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/2")

    with pytest.raises(ValueError):
        convert("1/-2")

    with pytest.raises(ValueError):
        convert("-1/-2")


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("3")

    with pytest.raises(ValueError):
        convert("1/2/3")

    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("1.5/3")

    with pytest.raises(ValueError):
        convert("3/2.5")


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_normal():
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"