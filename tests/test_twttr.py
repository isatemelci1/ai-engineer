from twttr import shorten

def test_lowercase_vowels():
    assert shorten("aeiou") == ""
    assert shorten("hello") == "hll"


def test_uppercase_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("HELLO") == "HLL"


def test_mixed_case():
    assert shorten("ApPlE") == "pPl"


def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"


def test_consonants():
    assert shorten("bcdfg") == "bcdfg"


def test_empty_string():
    assert shorten("") == ""

def test_y():
    assert shorten("rhythm") == "rhythm"
    assert shorten("yellow") == "yllw"