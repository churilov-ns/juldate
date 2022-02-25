from datetime import datetime
import numpy as np


list_datetime = [
    datetime(1, 1, 1),
    datetime(1, 1, 1, 6),
    datetime(1, 1, 1, 12),
    datetime(1, 1, 1, 18),
    datetime(1917, 4, 30, 13, 28, 54),
    datetime(2016, 2, 29, 9, 11, 31),
    datetime(2021, 10, 5, 22, 3, 12),
]

list_datetime64 = [
    np.datetime64('0001-01-01 00'),
    np.datetime64('0001-01-01 06'),
    np.datetime64('0001-01-01 12'),
    np.datetime64('0001-01-01 18'),
    np.datetime64('1917-04-30 13:28:54'),
    np.datetime64('2016-02-29 09:11:31'),
    np.datetime64('2021-10-05 22:03:12'),
]

list_datetime_all = list_datetime + list_datetime64

list_jd = [
    1721425.5,
    1721425.75,
    1721426.0,
    1721426.25,
    2421349.061736111,
    2457447.882997685,
    2459493.418888889,
]

list_mjd = [
    -678575.0,
    -678574.75,
    -678574.5,
    -678574.25,
    21348.561736111064,
    57447.382997685110,
    59492.918888888790,
]

tol = 1.e-9
