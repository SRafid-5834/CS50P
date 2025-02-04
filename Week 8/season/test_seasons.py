from datetime import date
from seasons import calc_mins


def test_calc_mins():
    assert calc_mins(date(2000, 1, 1), date(1999, 1, 1)) == 525600
    # assert calc_mins(date(2000, 1, 1), date(1998, 1, 1)) == 1051200
    assert calc_mins(date(2000, 1, 1), date(1995, 1, 1)) == 2629440
