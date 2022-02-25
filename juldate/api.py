"""
Functions for conversion between Julian date and other date/time
representations.

Available functions:
    datetime_to_jd: Convert given date and time to Julian day.
    jd_to_datetime: Convert given Julian day to datetime object.
    jd_to_datetime64: Convert given Julian day to numpy.datetime64 object.
    datetime_to_jd_v: Vectorized version of 'datetime_to_jd'.
    jd_to_datetime_v: Vectorized version of 'jd_to_datetime'.
    jd_to_datetime64_v: Vectorized version of 'jd_to_datetime64'.
"""


from typing import Union
from datetime import datetime
import numpy as np

from . import _utils as _u


__all__ = [
    'datetime_to_jd',
    'jd_to_datetime',
    'jd_to_datetime64',
    'datetime_to_jd_v',
    'jd_to_datetime_v',
    'jd_to_datetime64_v',
]


def datetime_to_jd(
    dt: _u.AnyDatetime,
    origin: Union[str, _u.AnyNumber] = 0,
) -> np.longdouble:
    """
    Convert given date and time to Julian day.

    Args:
        dt: Date and time to convert.
        origin: Epoch (in standard Julian days) from which Julian days count
            starts.

            Allowed values are 'jd', 'mjd' and any numeric value. 'jd' stands
            for standard Julian day, 'mjd' - for Modified Julian day. Default
            value is 0.

    Raises:
        ValueError: If provided origin type is unsupported.

    Returns:
        Julian day.
    """

    if isinstance(dt, np.datetime64):
        dt = dt.astype(datetime)
    return np.longdouble(_u.date_to_jdn(dt.year, dt.month, dt.day)) - \
        _u.get_origin_offset(origin) + \
        _u.time_to_jd_part(dt.hour, dt.minute, dt.second, dt.microsecond)


def jd_to_datetime(
    jd: _u.AnyNumber,
    origin: Union[str, _u.AnyNumber] = 0,
) -> datetime:
    """
    Convert given Julian day to datetime object.

    Args:
        jd: Julian day to convert.
        origin: Epoch (in standard Julian days) from which Julian days count
            starts.

            Allowed values are 'jd', 'mjd' and any numeric value. 'jd' stands
            for standard Julian day, 'mjd' - for Modified Julian day. Default
            value is 0.

    Raises:
        ValueError: If provided origin type is unsupported.

    Returns:
        Corresponding datetime object.
    """

    jd += _u.get_origin_offset(origin)
    jdn = int(jd)
    jd -= jdn
    if jd >= 0.5:
        jd -= 1
        jdn += 1

    return datetime(
        *_u.jdn_to_date(jdn),
        *_u.jd_part_to_time(jd),
    )


def jd_to_datetime64(
    jd: _u.AnyNumber,
    origin: Union[str, _u.AnyNumber] = 0,
) -> np.datetime64:
    """
    Convert given Julian day to numpy.datetime64 object.

    Args:
        jd: Julian day to convert.
        origin: Epoch (in standard Julian days) from which Julian days count
            starts.

            Allowed values are 'jd', 'mjd' and any numeric value. 'jd' stands
            for standard Julian day, 'mjd' - for Modified Julian day. Default
            value is 0.

    Raises:
        ValueError: If provided origin type is unsupported.

    Returns:
        Corresponding numpy.datetime64 object.
    """

    return np.datetime64(jd_to_datetime(jd, origin))


datetime_to_jd_v = np.vectorize(datetime_to_jd, excluded=['origin'])
jd_to_datetime_v = np.vectorize(jd_to_datetime, excluded=['origin'])
jd_to_datetime64_v = np.vectorize(jd_to_datetime64, excluded=['origin'])
