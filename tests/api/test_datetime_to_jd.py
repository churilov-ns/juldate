import pytest
import numpy as np
from juldate import datetime_to_jd, datetime_to_jd_v
from conftest import (
    list_datetime64,
    list_datetime_all,
    list_jd,
    list_mjd,
    tol,
)


@pytest.mark.parametrize(
    'dt, expected',
    [(d, e) for d, e in zip(list_datetime_all, list_jd * 2)],
)
def test_origin_jd(dt, expected):
    assert datetime_to_jd(dt, 'jd') == pytest.approx(expected, abs=tol)


@pytest.mark.parametrize(
    'dt, expected',
    [(d, e) for d, e in zip(list_datetime_all, list_mjd * 2)],
)
def test_origin_mjd(dt, expected):
    assert datetime_to_jd(dt, 'mjd') == pytest.approx(expected, abs=tol)


@pytest.mark.parametrize(
    'dt, expected',
    [(d, e) for d, e in zip(list_datetime_all, list_mjd * 2)],
)
def test_custom_origin(dt, expected):
    origin = datetime_to_jd(np.datetime64('1858-11-21 00'))
    assert datetime_to_jd(dt, origin) == pytest.approx(
        expected - 4.0,
        abs=tol,
    )


def test_vectorized():
    results = datetime_to_jd_v(list_datetime64, 'jd')
    for res, exp in zip(results, list_jd):
        assert res == pytest.approx(exp, abs=tol)
