from fuel import convert, gauge
import pytest


def test_convert():
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("4/1")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

    assert convert("3/4") == 75


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
