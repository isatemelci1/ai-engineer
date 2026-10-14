from plates import is_valid


def test_length():
    assert not is_valid("")
    assert not is_valid("A")
    assert is_valid("AB")
    assert is_valid("ABC123")
    assert not is_valid("ABC1234")


def test_first_two_characters():
    assert is_valid("CS")
    assert not is_valid("C5")
    assert not is_valid("5C")
    assert not is_valid("C50")
    assert not is_valid("5000")


def test_numbers():
    assert is_valid("CS50")
    assert is_valid("AB12")
    assert is_valid("CS2")
    assert not is_valid("CS05")
    assert not is_valid("CS50A")


def test_punctuation():
    assert is_valid("CS50")
    assert not is_valid("CS-50")
    assert not is_valid("CS 50")
    assert not is_valid("CS.50")
    assert not is_valid("CS!50")