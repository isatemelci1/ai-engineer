import pytest
from professor import generate_integer


def test_generate_integer_invalid_level():
    with pytest.raises(ValueError):
        generate_integer(5)


def test_generate_integer_level_two():
    for _ in range(100):
        number = generate_integer(2)
        assert 10 <= number <= 99