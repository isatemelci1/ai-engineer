import pytest
from calculator import square

""" def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared should be 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared should be 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared should be 4")
    try:
        assert square(5) == 25
    except AssertionError:
        print("5 squared should be 25")

if __name__ == "__main__":
    main() """

def test_positive_square():
    assert square(2) == 4
    assert square(3) == 9

def test_negative_square():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero_square():
    assert square(0) == 0

def test_str():
     with pytest.raises(TypeError):
        square("cat")