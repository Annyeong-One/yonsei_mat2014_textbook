# unittest Basics


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Introduction to Python's built-in unittest framework.

## Creating Test Cases

Write test classes with unittest.

```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
```

```
test_add_negative (__main__.TestMath) ... ok
test_add_positive (__main__.TestMath) ... ok
test_add_zero (__main__.TestMath) ... ok
```

## setUp and tearDown

Use setUp and tearDown for test initialization and cleanup.

```python
import unittest

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Run before each test
        self.db = {}
        print("Setting up test database")
    
    def tearDown(self):
        # Run after each test
        self.db.clear()
        print("Cleaning up database")
    
    def test_insert(self):
        self.db['user1'] = 'Alice'
        self.assertEqual(self.db['user1'], 'Alice')
    
    def test_delete(self):
        self.db['user1'] = 'Bob'
        del self.db['user1']
        self.assertNotIn('user1', self.db)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
```

```
Setting up test database
test_delete (__main__.TestDatabase) ... ok
Cleaning up database
test_insert (__main__.TestDatabase) ... ok
```

