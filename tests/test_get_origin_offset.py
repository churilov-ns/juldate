import pytest
from juldate._utils import get_origin_offset


@pytest.mark.parametrize(
    'origin,expected',
    [
        ('jd', 0),
        ('mjd', 2400000.5),
        ('cnes', 2433282.5),
        (100500.5, 100500.5),
    ],
)
def test_get_origin_offset(origin, expected):
    assert get_origin_offset(origin) == expected


def test_get_unsupported_origin_offset():
    with pytest.raises(ValueError):
        get_origin_offset('bad_origin')