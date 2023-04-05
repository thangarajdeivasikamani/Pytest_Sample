from sample_source import add,subtract,multiply,divide,maximum,minimum
import pytest


NUMBER_1 = 3.0
NUMBER_2 = 2.0
NUMBER_4 = 12.0
NUMBER_5 = 2.0


def test_add():
    value = add(NUMBER_1, NUMBER_2)
    assert value == 5.0


def test_subtract():
    value = subtract(NUMBER_1, NUMBER_2)
    assert value == 1.0


def test_subtract_negative():
    value = subtract(NUMBER_2, NUMBER_1)
    assert value == -1.0


def test_multiply():
    value = multiply(NUMBER_1, NUMBER_2)
    assert value == 6.0


def test_divide():
    value = divide(NUMBER_1, NUMBER_2)
    assert value == 1.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        divide(NUMBER_1, 0)
    assert "division by zero" in str(e.value)


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_4, NUMBER_5, NUMBER_4),
    (NUMBER_5, NUMBER_4, NUMBER_1), # will fail, updated as (NUMBER_5, NUMBER_4, NUMBER_4) will pass
    (NUMBER_4, NUMBER_4, NUMBER_4),
    (NUMBER_5, NUMBER_5, NUMBER_5),
])
def test_maximum(a, b, expected):
    assert maximum(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_2),
    (NUMBER_2, NUMBER_1, NUMBER_2),
    (NUMBER_2, NUMBER_2, NUMBER_2),
])
def test_minimum(a, b, expected):
    assert minimum(a, b) == expected