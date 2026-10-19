
from datetime import date

from seasons import minutes_between, minutes_in_words


def test_minutes_between_one_day():
    assert minutes_between(date(2000, 1, 1), date(2000, 1, 2)) == 1440


def test_minutes_between_one_year():
    assert minutes_between(date(2000, 1, 1), date(2001, 1, 1)) == 527040


def test_minutes_between_same_day():
    assert minutes_between(date(2000, 1, 1), date(2000, 1, 1)) == 0


def test_minutes_in_words():
    assert minutes_in_words(525600) == (
        "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_minutes_in_words_zero():
    assert minutes_in_words(0) == "Zero minutes"
