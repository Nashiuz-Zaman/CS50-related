from working import convert
import pytest


def test_invalid_string():
    with pytest.raises(ValueError):
        convert('Cat')


def test_invalid_format():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("1:80 AM to 5:30 PM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("20 PM to 40 PM")


def test_valid_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
