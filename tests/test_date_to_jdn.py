import pytest
from juldate._utils import date_to_jdn


@pytest.mark.parametrize(
    'year, month, day, expected',
    [
        (-4713, 11, 24, 0),
        (-2020, 2, 24, 983324),
        (-1, 8, 15, 1720921),
        (1, 1, 2, 1721427),
        (1917, 5, 11, 2421360),
        (2016, 2, 29, 2457448),
        (2020, 1, 1, 2458850),
    ]
)
def test_date_to_jdn(year, month, day, expected):
    assert date_to_jdn(year, month, day) == pytest.approx(expected, abs=1.e-5)
