# unittest.TestCase Methods


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Common assertion methods provided by TestCase.

## Equality and Comparison Assertions

Assert equality and inequality.

```python
import unittest

class TestAssertions(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(5, 5)
    
    def test_not_equal(self):
        self.assertNotEqual(5, 3)
    
    def test_greater(self):
        self.assertGreater(10, 5)
    
    def test_less(self):
        self.assertLess(3, 5)
    
    def test_almost_equal(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=2)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
```

```
test_almost_equal ... ok
test_equal ... ok
test_greater ... ok
test_less ... ok
test_not_equal ... ok
```

## Container and Type Assertions

Assert membership, containment, and types.

```python
import unittest

class TestContainers(unittest.TestCase):
    def test_in(self):
        self.assertIn(2, [1, 2, 3])
    
    def test_not_in(self):
        self.assertNotIn(4, [1, 2, 3])
    
    def test_is_instance(self):
        self.assertIsInstance("hello", str)
    
    def test_is_none(self):
        self.assertIsNone(None)
    
    def test_is_not_none(self):
        self.assertIsNotNone(42)
    
    def test_true(self):
        self.assertTrue(5 > 3)
    
    def test_false(self):
        self.assertFalse(5 < 3)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
```

```
test_false ... ok
test_in ... ok
test_is_instance ... ok
test_is_none ... ok
test_is_not_none ... ok
test_true ... ok
```

