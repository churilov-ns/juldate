from datetime import datetime
import pytest
import numpy as np
from juldate import datetime_to_jd, datetime_to_jd_v


test_datetimes = [
    datetime(1, 1, 1),
    datetime(1, 1, 1, 6),
    datetime(1, 1, 1, 12),
    datetime(1, 1, 1, 18),
    datetime(1917, 4, 30, 13, 28, 54),
    datetime(2016, 2, 29, 9, 11, 31),
    datetime(2021, 10, 5, 22, 3, 12),
]
test_datetimes64 = [
    np.datetime64('0001-01-01 00'),
    np.datetime64('0001-01-01 06'),
    np.datetime64('0001-01-01 12'),
    np.datetime64('0001-01-01 18'),
    np.datetime64('1917-04-30 13:28:54'),
    np.datetime64('2016-02-29 09:11:31'),
    np.datetime64('2021-10-05 22:03:12'),
]
test_input = test_datetimes + test_datetimes64
expected_jds = [
    1721425.5,
    1721425.75,
    1721426.0,
    1721426.25,
    2421349.061736111,
    2457447.882997685,
    2459493.418888889,
]
expected_mjds = [
    -678575.0,
    -678574.75,
    -678574.5,
    -678574.25,
    21348.561736111064,
    57447.382997685110,
    59492.918888888790,
]
tol = 1.e-9


@pytest.mark.parametrize(
    'dt, expected',
    [(d, e) for d, e in zip(test_input, expected_jds * 2)],
)
def test_origin_jd(dt, expected):
    assert datetime_to_jd(dt, 'jd') == pytest.approx(expected, abs=tol)


@pytest.mark.parametrize(
    'dt, expected',
    [(d, e) for d, e in zip(test_input, expected_mjds * 2)],
)
def test_origin_mjd(dt, expected):
    assert datetime_to_jd(dt, 'mjd') == pytest.approx(expected, abs=tol)


@pytest.mark.parametrize(
    'dt, expected',
    [(d, e) for d, e in zip(test_input, expected_mjds * 2)],
)
def test_custom_origin(dt, expected):
    origin = datetime_to_jd(np.datetime64('1858-11-21 00'))
    assert datetime_to_jd(dt, origin) == pytest.approx(
        expected - 4.0,
        abs=tol,
    )


def test_vectorized():
    results = datetime_to_jd_v(test_datetimes64, 'jd')
    for res, exp in zip(results, expected_jds):
        assert res == pytest.approx(exp, abs=1.e-9)
