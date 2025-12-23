from jar import Jar
import pytest

def test_init():
    jar1 = Jar(10)
    assert jar1.capacity == 10
    assert jar1.size == 0
    with pytest.raises(ValueError):
        Jar(-5)

def test_str():
    jar = Jar(10)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(8)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(4)
