# test_bank.py

from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("Hello, John") == 0
    assert value(" hello   ") == 0



def test_h():
    assert value("h") == 20
    assert value("H") == 20
    assert value("  h    ") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20
    assert value("How you doing?") == 20


def test_other():
    assert value("What's happening?") == 100
    assert value("  jv k7tmni udfg4 asdf58  ") == 100
    assert value("What's up?") == 100
