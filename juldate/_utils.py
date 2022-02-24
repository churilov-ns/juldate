"""
Helper functions and variables to provide conversions.
"""


from typing import Union
from numbers import Number
import numpy as np


AnyNumber = Union[Number, np.number]


_float = np.longdouble
_DAY_HOUR = np.longdouble(24.0)
_DAY_MIN = np.longdouble(1440.0)
_DAY_SEC = np.longdouble(86400.0)
_DAY_MSEC = _DAY_SEC * 1000


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


def date_to_jd(year: int, month: int, day: int) -> _float:
    m = int((month - 14) / 12)
    ypm = year + m
    tmp = (1461 * (ypm + 4800)) // 4 + \
          (367 * (month - 2 - 12 * m)) // 12 - \
          (3 * ((ypm + 4900) // 100)) // 4 + day
    return _float(tmp) - _float(32075.5)


def time_to_jd(
    hour: int,
    minute: int,
    second: int,
    microsecond: int,
) -> _float:
    return _float(hour) / _DAY_HOUR + \
        _float(minute) / _DAY_MIN + \
        _float(second) / _DAY_SEC + \
        _float(microsecond) / _DAY_MSEC
