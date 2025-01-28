# test_plates.py

from plates import is_valid


def test_initial_two():
    assert is_valid("CS") == True
    assert is_valid("C1") == False
    assert is_valid("1S") == False
    # assert is_valid("   CS   ") == True
    # assert is_valid("cs") == True


def test_length():
    assert is_valid("H") == False
    assert is_valid("CS50000") == False
    assert is_valid("OUTATIME") == False


def test_combo():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CSCSCS") == True
    assert is_valid("AA2222") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


def test_invalid_cahr():
    assert is_valid("PI3.14") == False
