from numb3rs import validate


def test_not_digit():
    assert validate("cat") is False
    assert validate("   a.b.c.d   ") is False
    assert validate("   aaa.bbb.ccc.ddd   ") is False
    assert validate("a.b.1.2") is False



def test_invalid_digits():
    assert validate("-1.-1.-1.-1") is False
    assert validate("1.1.1.1.1") is False
    assert validate("1.1.1") is False
    assert validate("256.256.256.256") is False
    assert validate("255.256.256.256") is False
    assert validate("273.3.6.28") is False


def test_valid():
    assert validate("0.0.0.0") is True
    assert validate("1.2.3.4") is True
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
