import pytest
import sys


def add(a, b=3):
    return a + b


def multiply(x, y=2):
    return x * y


@pytest.mark.numbers
def test_add():
    assert add(3, 5) == 8
    assert add(7) == 10


@pytest.mark.strings
def test_add_string():
    assert add("Hello ") == "Hello Hello "


@pytest.mark.skipif(sys.version_info < (3, 3), reason="Learning To Skip Tests")
def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(9) == 18
