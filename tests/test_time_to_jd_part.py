import pytest
from juldate._utils import time_to_jd_part


@pytest.mark.parametrize(
    'hour, minute, second, msec, expected',
    [
        (0, 0, 0, 0, -0.5),
        (6, 0, 0, 0, -0.25),
        (12, 0, 0, 0, 0.0),
        (0, 720, 0, 0, 0.0),
        (0, 0, 43200, 0, 0.0),
        (0, 0, 0, 43200000, 0.0),
        (18, 0, 0, 0, 0.25),
    ]
)
def test_time_to_jd_part(hour, minute, second, msec, expected):
    result = time_to_jd_part(hour, minute, second, msec)
    assert result == pytest.approx(expected, abs=1.e-5)
