from twttr import shorten


def test_letters():
    assert shorten("Short") == "Shrt"
    assert shorten("ShOrt") == "Shrt"
    assert shorten("Angel") == "ngl"


def test_numbers():
    assert shorten("123") == "123"


def test_punctuations():
    assert shorten("bcd.") == "bcd."
