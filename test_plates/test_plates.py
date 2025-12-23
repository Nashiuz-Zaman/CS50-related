from plates import is_valid


def test_one():
    assert is_valid("CS50") == True


def test_two():
    assert is_valid("CS05") == False


def test_three():
    assert is_valid("CS50P") == False


def test_length():
    assert is_valid("A") == False


def test_beginning_alphabetical():
    assert is_valid("CS") == True
    assert is_valid("11") == False
    assert is_valid("??") == False


def test_alpha_numeric():
    assert is_valid("AA-A") == False
