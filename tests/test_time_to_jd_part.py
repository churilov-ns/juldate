import pytest
from juldate._utils import time_to_jd_part, jd_part_to_time


test_data = [
    (0, 0, 0, 0, -0.5),
    (6, 0, 0, 0, -0.25),
    (12, 0, 0, 0, 0.0),
    (12, 25, 0, 0, 0.017361111),
    (12, 0, 45, 0, 0.000520833),
    (12, 0, 0, 800, 0.000009259),
    (18, 0, 0, 0, 0.25),
]
tol = 1.e-9


@pytest.mark.parametrize(
    'hour, minute, second, msec, jd_part',
    test_data,
)
def test_time_to_jd_part(hour, minute, second, msec, jd_part):
    result = time_to_jd_part(hour, minute, second, msec)
    assert result == pytest.approx(jd_part, abs=tol)


@pytest.mark.parametrize(
    'hour, minute, second, msec, _',
    test_data,
)
def test_jd_part_to_time(hour, minute, second, msec, _):
    jd_part = time_to_jd_part(hour, minute, second, msec)
    result = jd_part_to_time(jd_part)
    assert result == (hour, minute, second, msec)
