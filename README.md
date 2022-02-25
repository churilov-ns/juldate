Juldate
=======
This package is intended for conversion between Julian date and other 
date/time representations, like datetime and numpy.datetime64 objects.

## Installation
```commandline
git clone https://github.com/churilov-ns/juldate.git
cd juldate
pip install -e .[dev]
```

## Running tests
```commandline
pytest ./tests
```

## Usage example
```python
from datetime import datetime
import juldate


dt = datetime.now()
jd = juldate.datetime_to_jd(dt)
mjd = juldate.datetime_to_jd(dt, 'mjd')
```
