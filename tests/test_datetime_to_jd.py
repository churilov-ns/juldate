from datetime import datetime
import pytest
import numpy as np
from juldate import datetime_to_jd, datetime_to_jd_v


@pytest.mark.parametrize(
    'dt, expected',
    [
        (datetime(1, 1, 1), 1721425.5),
        (np.datetime64('0001-01-01 00'), 1721425.5),
        (datetime(1, 1, 1, 6), 1721425.75),
        (np.datetime64('0001-01-01 06'), 1721425.75),
        (datetime(1, 1, 1, 12), 1721426.0),
        (np.datetime64('0001-01-01 12'), 1721426.0),
        (datetime(1, 1, 1, 18), 1721426.25),
        (np.datetime64('0001-01-01 18'), 1721426.25),
        (datetime(1917, 4, 30, 13, 28, 54), 2421349.061736111),
        (np.datetime64('1917-04-30 13:28:54'), 2421349.061736111),
        (datetime(2016, 2, 29, 9, 11, 31), 2457447.882997685),
        (np.datetime64('2016-02-29 09:11:31'), 2457447.882997685),
        (datetime(2021, 10, 5, 22, 3, 12), 2459493.418888889),
        (np.datetime64('2021-10-05 22:03:12'), 2459493.418888889),
    ]
)
def test_origin_jd(dt, expected):
    assert datetime_to_jd(dt, 'jd') == pytest.approx(expected, abs=1.e-9)


@pytest.mark.parametrize(
    'dt, expected',
    [
        (datetime(1, 1, 1), -678575.0),
        (np.datetime64('0001-01-01 00'), -678575.0),
        (datetime(1, 1, 1, 6), -678574.75),
        (np.datetime64('0001-01-01 06'), -678574.75),
        (datetime(1, 1, 1, 12), -678574.5),
        (np.datetime64('0001-01-01 12'), -678574.5),
        (datetime(1, 1, 1, 18), -678574.25),
        (np.datetime64('0001-01-01 18'), -678574.25),
        (datetime(1917, 4, 30, 13, 28, 54), 21348.561736111064),
        (np.datetime64('1917-04-30 13:28:54'), 21348.561736111064),
        (datetime(2016, 2, 29, 9, 11, 31), 57447.38299768511),
        (np.datetime64('2016-02-29 09:11:31'), 57447.38299768511),
        (datetime(2021, 10, 5, 22, 3, 12), 59492.91888888879),
        (np.datetime64('2021-10-05 22:03:12'), 59492.91888888879),
    ]
)
def test_origin_mjd(dt, expected):
    assert datetime_to_jd(dt, 'mjd') == pytest.approx(expected, abs=1.e-9)


def test_vectorized():
    dts = np.array([
        '0001-01-01 00',
        '0001-01-01 06',
        '0001-01-01 12',
        '0001-01-01 18',
        '1917-04-30 13:28:54',
        '2016-02-29 09:11:31',
        '2021-10-05 22:03:12',
    ], dtype=np.datetime64)

    expected = [
        1721425.5,
        1721425.75,
        1721426.0,
        1721426.25,
        2421349.061736111,
        2457447.882997685,
        2459493.418888889,
    ]

    for res, exp in zip(datetime_to_jd_v(dts, 'jd'), expected):
        assert res == pytest.approx(exp, abs=1.e-9)
