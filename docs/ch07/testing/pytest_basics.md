# pytest Basics

Introduction to pytest, a simpler and more powerful testing framework.

## Simple pytest Tests

Write tests without unittest boilerplate.

```python
# test_math.py - pytest style
def add(a, b):
    return a + b

def test_addition():
    assert add(2, 3) == 5

def test_negative():
    assert add(-1, 1) == 0

def test_string_concat():
    assert add("hello", " world") == "hello world"

# Run with: pytest test_math.py -v
```

```
test_math.py::test_addition PASSED
test_math.py::test_negative PASSED
test_math.py::test_string_concat PASSED
```

## pytest Markers and Organization

Organize tests with markers and fixtures.

```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(0.1)
    assert True

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add(a, b, expected):
    assert a + b == expected

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

# Run with: pytest -v -m "not slow"
print("pytest organization example")
```

```
pytest organization example
```

