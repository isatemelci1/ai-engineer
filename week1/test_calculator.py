import calculator

def test_average():
    assert calculator.average(2, 4) == 3
    assert calculator.average(0, 0) == 0
    assert calculator.average(-2, 2) == 0
    assert calculator.average(5, 5) == 5

def test_total():
    assert calculator.total(2, 4) == 6
    assert calculator.total(0, 0) == 0
    assert calculator.total(-2, 2) == 0
    assert calculator.total(5, 5) == 10

def test_difference():
    assert calculator.difference(2, 4) == -2
    assert calculator.difference(0, 0) == 0
    assert calculator.difference(-2, 2) == -4
    assert calculator.difference(5, 5) == 0