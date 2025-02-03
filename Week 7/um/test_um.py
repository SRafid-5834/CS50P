from um import count


def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um, ") == 1
    assert count("um um um") == 3
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_not_um():
    assert count("yum") == 0
    assert count("hello world") == 0
    assert count("123456789") == 0


def test_edge():
    assert count("umum") == 0
    assert count("helloumworld") == 0
