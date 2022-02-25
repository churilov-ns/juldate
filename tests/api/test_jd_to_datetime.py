import pytest
import numpy as np
from juldate import (
    datetime_to_jd,
    jd_to_datetime,
    jd_to_datetime64,
    jd_to_datetime_v,
    jd_to_datetime64_v,
)
from conftest import (
    list_datetime,
    list_datetime64,
    list_jd,
    list_mjd,
)


@pytest.mark.parametrize(
    'dt, jd',
    [(dt, jd) for dt, jd in zip(list_datetime, list_jd)],
)
def test_origin_jd(dt, jd):
    assert jd_to_datetime(jd, 'jd') == dt


@pytest.mark.parametrize(
    'dt, jd',
    [(dt, jd) for dt, jd in zip(list_datetime64, list_jd)],
)
def test_origin_jd_64(dt, jd):
    assert jd_to_datetime64(jd, 'jd') == dt


@pytest.mark.parametrize(
    'dt, jd',
    [(dt, jd) for dt, jd in zip(list_datetime, list_mjd)],
)
def test_origin_mjd(dt, jd):
    assert jd_to_datetime(jd, 'mjd') == dt


@pytest.mark.parametrize(
    'dt, jd',
    [(dt, jd) for dt, jd in zip(list_datetime64, list_mjd)],
)
def test_origin_mjd_64(dt, jd):
    assert jd_to_datetime64(jd, 'mjd') == dt


@pytest.mark.parametrize(
    'dt, jd',
    [(dt, jd) for dt, jd in zip(list_datetime, list_mjd)],
)
def test_custom_origin(dt, jd):
    origin = datetime_to_jd(np.datetime64('1858-11-21 00'))
    assert (jd_to_datetime(jd, origin) - dt).total_seconds() == 4 * 86400


def test_vectorized():
    results = jd_to_datetime_v(list_jd, 'jd')
    for res, exp in zip(results, list_datetime):
        assert res == exp


def test_vectorized_64():
    results = jd_to_datetime64_v(list_jd, 'jd')
    for res, exp in zip(results, list_datetime64):
        assert res == exp
