"""
Helper functions and variables to provide conversions.
"""


from typing import Union, Tuple
from datetime import datetime
from numbers import Number
import numpy as np


AnyNumber = Union[Number, np.number]
AnyDatetime = Union[datetime, np.datetime64]


_float = np.longdouble
_DAY_HOUR = _float(24.0)
_DAY_MIN = _float(1440.0)
_DAY_SEC = _float(86400.0)
_DAY_MSEC = _DAY_SEC * _float(1000)


ORIGINS = {
    'jd': _float(0.0),
    'mjd': _float(2400000.5),
}


def get_origin_offset(origin: Union[str, AnyNumber]) -> _float:
    """
    Get offset in days for given origin.

    Args:
        origin: Origin type or offset itself.

    Raises:
        ValueError: If provided origin is unsupported.

    Returns:
        Offset in days.
    """

    if isinstance(origin, str):
        try:
            return ORIGINS[origin]
        except KeyError as e:
            raise ValueError(f'Unsupported origin type: {origin}') from e
    else:
        return _float(origin)


def date_to_jdn(year: int, month: int, day: int) -> int:
    """
    Convert calendar date to Julian day number.

    Args:
        year: Year number.
        month: Month in year.
        day: Day in month.

    Returns:
        Julian day number.
    """
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    return day + (153 * m + 2) // 5 + \
        365 * y + y // 4 - y // 100 + y // 400 - 32045


def jdn_to_date(jdn: int) -> Tuple[int, int, int]:
    """
    Convert Julian day number to calendar date.

    Args:
        jdn: Julian day number.

    Returns:
        Year, month and day.
    """

    a = jdn + 32044
    b = (4 * a + 3) // 146097
    c = a - (146097 * b) // 4
    d = (4 * c + 3) // 1461
    e = c - (1461 * d) // 4
    m = (5 * e + 2) // 153

    return (
        100 * b + d - 4800 + m // 10,
        m + 3 - 12 * (m // 10),
        e - (153 * m + 2) // 5 + 1,
    )


def time_to_jd_part(
    hour: int,
    minute: int,
    second: int,
    microsecond: int,
) -> _float:
    """
    Convert human time to day fraction with -12 hours offset (Julian dates
    count starts at 12 am).

    Args:
        hour: Hour.
        minute: Minute.
        second: Second.
        microsecond: Microsecond.

    Returns:
        Julian date part for given time.
    """

    return _float(hour - 12) / _DAY_HOUR + \
        _float(minute) / _DAY_MIN + \
        _float(second) / _DAY_SEC + \
        _float(microsecond) / _DAY_MSEC


def jd_part_to_time(jd_part: AnyNumber) -> Tuple[int, int, int, int]:
    """
    Convert day fraction to human time.

    Args:
        jd_part: Julian date part.

    Returns:
        Hour, Minute, Second and Microsecond.
    """

    jd_part += 12 / _DAY_HOUR
    assert jd_part >= _float(0.0)

    hours = int(jd_part * _DAY_HOUR)
    jd_part -= hours / _DAY_HOUR
    minutes = int(jd_part * _DAY_MIN)
    jd_part -= minutes / _DAY_MIN
    seconds = int(jd_part * _DAY_SEC)
    jd_part -= seconds / _DAY_SEC
    microseconds = int(np.rint(jd_part * _DAY_MSEC))

    if microseconds > 999:
        microseconds = 0
        seconds += 1
        if seconds > 59:
            seconds = 0
            minutes += 1
            if minutes > 59:
                minutes = 0
                hours += 1

    return hours, minutes, seconds, microseconds
