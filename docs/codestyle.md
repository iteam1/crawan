Maximum 80 characters per line.


---
```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

```python
foo = long_function_name(
    var_one, var_two,
    var_three, var_four
)
```
---

```python
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```
---

```python
if (this_is_one_thing and
    that_is_another_thing):
    do_something()
```
---

```python
my_list = [
    1, 2, 3,
    4, 5, 6,
]
```
---

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```
---

```python
income = (
  gross_wages
  + taxable_interest
  + (dividends - qualified_dividends)
  - ira_deduction
  - student_loan_interest
)
```
---

```python
import os
import sys
```

```python
from subprocess import Popen, PIPE
```
---

```python
if x == 4: print x, y; x, y = y, x
```
---

```python
spam(ham[1], {eggs: 2})
```

```python
spam(1)
```


```python
dct['key'] = lst[index]
```


```python
x = 1
y = 2
long_variable = 3
```


```python
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
---

```python
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...
```

```python
def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
```
---

```python
from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```
---

Yes:
```python
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
```

Rather not:
```python
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()

if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()
```

Definitely not:
```python
if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()
```
---

Package and Module Names

* do_blah_thing, convert

Class Names

* DoBlahThing, Convert

---

Yes:
```python
if foo is not None:
```

No:
```python
if not foo is None:
```
---

Yes:
```python
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
```

No:
```python
try:
    # Too broad!
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    return key_not_found(key)
```
---

Yes:
```python
if not seq:
if seq:
```

No:
```python
if len(seq):
if not len(seq):
```
---

Yes:
```python
if greeting:
```

No:
```python
if greeting == True:
```

Worse:
```python
if greeting is True:
```
---

```python
def foo():
    """
    Calculate something and return the result.
    """
    ...
```
---

```python
# Future
from __future__ import unicode_literals

# Standard Library
import json
from itertools import chain

# Third-Party
import bcrypt

# Django
from django.http import Http404
from django.http.response import (
    Http404, HttpResponse, HttpResponseNotAllowed, StreamingHttpResponse,
    cookie,
)

# Local Django
from .models import LogEntry

# try/except
try:
    import yaml
except ImportError:
    yaml = None

CONSTANT = 'foo'


class Example(object):
    # ...
```
---

Yes:
```python
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
```

No:
```python
class Person(models.Model):
    FirstName = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=40)
```
---

Yes:
```python
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'people'
```

No:
```python
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    class Meta:
        verbose_name_plural = 'people'
```

```python
class Person(models.Model):
    class Meta:
        verbose_name_plural = 'people'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
```
---

Model Class Order
* All database fields
* Custom manager attributesM˜
* class Meta
* def __str__()
* def save()
* def get_absolute_url()
* Any custom methods

---

```
announce = CourseBasedAnnounce.objects \
    .by_user_course(user=user, course=course) \
    .select_related('course') \
    .first()
```
---

```python
{{ foo }}
```
---