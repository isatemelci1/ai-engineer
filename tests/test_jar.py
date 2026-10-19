
import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar(2.5)

    with pytest.raises(ValueError):
        Jar(True)


def test_read_only_properties():
    jar = Jar(5)

    with pytest.raises(AttributeError):
        jar.capacity = 10

    with pytest.raises(AttributeError):
        jar.size = 3


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪" * 12


def test_deposit():
    jar = Jar(3)

    jar.deposit(2)
    assert jar.size == 2

    # Depositing exactly to capacity is valid.
    jar.deposit(1)
    assert jar.size == 3

    # Depositing beyond capacity is invalid.
    with pytest.raises(ValueError):
        jar.deposit(1)

    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(3)

    jar.withdraw(2)
    assert jar.size == 1

    # Withdrawing exactly what's left is valid.
    jar.withdraw(1)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)

    with pytest.raises(ValueError):
        jar.withdraw(-1)


def test_invalid_amount_types():
    jar = Jar(5)

    for amount in (1.5, "2", None, True):
        with pytest.raises(ValueError):
            jar.deposit(amount)

        with pytest.raises(ValueError):
            jar.withdraw(amount)
