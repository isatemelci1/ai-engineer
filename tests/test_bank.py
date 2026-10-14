from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, Newman") == 0


def test_starts_with_h():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("Howdy") == 20
    assert value("h") == 20


def test_other_greetings():
    assert value("Good morning") == 100
    assert value("What's up?") == 100
    assert value("welcome") == 100


def test_empty_string():
    assert value("") == 100