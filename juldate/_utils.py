"""
Helper functions and variables to provide conversions.
"""


from typing import Union
from numbers import Number
import numpy as np


AnyNumber = Union[Number, np.number]


_float = np.longdouble
_DAY_HOUR = _float(24.0)
_DAY_MIN = _float(1440.0)
_DAY_SEC = _float(86400.0)
_DAY_MSEC = _DAY_SEC * _float(1000)


ORIGINS = {
    'jd': _float(0.0),
    'mjd': _float(2400000.5),
    'cnes': _float(2433282.5),
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
    jdn = day + (153 * m + 2) // 5 + \
        365 * y + y // 4 - y // 100 + y // 400 - 32045
    return jdn if year < 0 else jdn - 1


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
