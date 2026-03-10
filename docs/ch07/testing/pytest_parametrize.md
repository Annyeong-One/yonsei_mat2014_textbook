# pytest Parametrize


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Use parametrize to test multiple input/output combinations efficiently.

## Basic Parametrization

Test multiple inputs with a single test function.

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (9, 3, 3),
    (8, 4, 2),
    (0, 5, 0),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

# Run with: pytest -v test_divide.py
print("Parametrization test")
```

```
Parametrization test
```

## Parametrizing with pytest.param

Use pytest.param for complex parametrization.

```python
import pytest

def is_palindrome(text):
    return text == text[::-1]

@pytest.mark.parametrize("word,is_palindrome_expected", [
    ("racecar", True),
    ("hello", False),
    ("noon", True),
    ("a", True),
    pytest.param("", True, marks=pytest.mark.skip),
])
def test_palindrome(word, is_palindrome_expected):
    assert is_palindrome(word) == is_palindrome_expected

print("pytest.param allows custom marking")
```

```
pytest.param allows custom marking
```

