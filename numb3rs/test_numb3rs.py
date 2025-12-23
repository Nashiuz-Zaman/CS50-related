from numb3rs import validate


def test_valid_ip():
    assert validate('127.0.0.1') == True


def test_invalid_ip():
    assert validate('512.512.512.512') == False


def test_invalid_str():
    assert validate('cat') == False

def test_second_byte():
    assert validate('127.300.0.1') == False
