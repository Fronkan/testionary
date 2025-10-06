# Testionary

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A library providing tools to inspect dicionaries during testing. 

## Installation

Using pip:
```
pip install testionary
```
or using uv for project management:

```
uv add testionary
```

## Usage

### Read and Modified attributes
Accessing a value using e.g. the `[]`-operator or `dict.get()` method will cause the key to be added to `BasicTrackingDict.accessed_keys`. Setting a value e.g. using assignment together with the `[]`-operator will get tracked using `BasicTrackingDict.modified_keys`. Here is a small example:
```python
# My library code:
def set_danger(enemy):
    if enemy["type"] == "Rabbit":
        enemy["danger"] = 9000


# My test:
from testionary.basic import BasicTrackingDict

def test_set_danger():
    tracked_dict = BasicTrackingDict({"type": "Rabbit", "danger": 42})
    set_danger(tracked_dict)

    assert "type" in tracked_dict.accessed_keys
    assert "danger" in tracked_dict.modified_keys
```

#### Tracked Access methods
- `[]`
- `.get`


#### Tracked Modification methods
- `[] =`
- `.update()`
- `|=`

### Iteration
When iterating over dictionary, e.g. when using dictionary comprehension, you might be accessing a few or all of the items. However, in these scenarios it is common to actually interate over all the key-value pairs while filtering on some condition. Instead of attemting to track each access with `BasicTrackingDict.accessed_keys`, a boolean attribute, `BasicTrackingDict.has_been_iterated`, is used instead. Here is an example of this being used:
```python
# Libray code
def vals_as_str(_dict):
    return {k: str(v) for k,v in _dict.items()}

# My test:
from testionary.basic import BasicTrackingDict

def test_vals_as_str():
    tracked_dict = BasicTrackingDict({"type": "Rabbit", "danger": 42, "hp": 100, "armor": 100})
    vals_as_str(tracked_dict)

    assert tracked_dict.has_been_iterated
```

#### Tracked Iteration Methods
- `__iter__()` called by `iter()` and `for`
- `__contains__()`, called by `in` operator in e.g. `if "key" in my_dict`
- `.keys()`
- `.values()`
- `.items()`

For `.keys()`, `.values()`, and `.items()`, iteration is assumed following calls to these methods. The returned dict-views are not inspected.
