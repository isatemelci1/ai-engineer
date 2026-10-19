
from um import count


def test_inside_words():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("yummy album umbrella") == 0


def test_punctuation():
    assert count("um, um? ...um...") == 3


def test_case_insensitive():
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM Um UM") == 3


def test_start_and_end():
    assert count("um hello") == 1
    assert count("hello um") == 1
    assert count("um") == 1


def test_multiple_occurrences():
    assert count("um, I think, um, we should, um, go") == 3
    assert count("um um um um um") == 5
    assert count("no hesitation here") == 0
