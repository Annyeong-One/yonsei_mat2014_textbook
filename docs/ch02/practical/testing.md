# Testing

## Unit Tests

### 1. Basic

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)
```

### 2. Fixtures

```python
class TestCounter(unittest.TestCase):
    def setUp(self):
        self.counter = make_counter()
```

## Test Closures

### 1. State

```python
def test_closure():
    inc, get = make_counter()
    inc()
    assert get() == 1
```

## Summary

- Write tests
- Use fixtures
- Test state
