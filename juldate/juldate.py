"""
...
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
    dt: Union[datetime, np.datetime64],
    origin: Union[str, _u.AnyNumber] = 0,
) -> np.longdouble:
    if isinstance(dt, np.datetime64):
        dt = dt.astype(datetime)
    return _u.date_to_jd(dt.year, dt.month, dt.day) - \
        _u.get_origin_offset(origin) + \
        _u.time_to_jd(dt.hour, dt.minute, dt.second, dt.microsecond)


def jd_to_datetime(
    jd: _u.AnyNumber,
    origin: Union[str, _u.AnyNumber] = 0,
) -> datetime:
    pass


def jd_to_datetime64(
    jd: _u.AnyNumber,
    origin: Union[str, _u.AnyNumber] = 0,
) -> np.datetime64:
    pass


datetime_to_jd_v = np.vectorize(datetime_to_jd, excluded=['origin'])
jd_to_datetime_v = np.vectorize(jd_to_datetime, excluded=['origin'])
jd_to_datetime64_v = np.vectorize(jd_to_datetime64, excluded=['origin'])
