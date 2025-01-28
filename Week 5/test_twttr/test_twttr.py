# test_twttr.py

from twttr import shorten


def test_only_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("EIAUO") == ""


def test_only_consonants():
    assert shorten("qwrty") == "qwrty"
    assert shorten("BFXDV") == "BFXDV"


def test_only_nonletters():
    assert shorten("12345") == "12345"
    assert shorten("*/-+[}.>?,") == "*/-+[}.>?,"


def test_all():
    assert shorten("la49  */eblu SVE iko") == "l49  */bl SV k"
    assert shorten("What's your name? Agent 007?") == "Wht's yr nm? gnt 007?"
