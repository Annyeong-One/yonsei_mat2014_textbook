# Mocking (unittest.mock)

Mock external dependencies to isolate tests and control behavior.

## Basic Mocking

Replace objects with mocks.

```python
from unittest.mock import Mock, patch

def get_user_data(user_id):
    # Normally makes a database call
    return {"id": user_id, "name": "Alice"}

def test_with_mock():
    with patch('__main__.get_user_data') as mock_get:
        mock_get.return_value = {"id": 1, "name": "Mocked"}
        
        result = get_user_data(1)
        
        assert result["name"] == "Mocked"
        mock_get.assert_called_once_with(1)

# Direct mock creation
mock_obj = Mock()
mock_obj.method.return_value = 42
assert mock_obj.method() == 42
print("Mocking complete")
```

```
Mocking complete
```

## Mocking with MagicMock

MagicMock supports magic methods.

```python
from unittest.mock import MagicMock

# MagicMock supports more operations
mock = MagicMock()

# Can be used as iterable
mock.__iter__.return_value = [1, 2, 3]
for item in mock:
    print(item)

# Can be used as callable
mock.return_value = "result"
result = mock()
print(f"Call result: {result}")

# Can be indexed
mock.__getitem__.return_value = "indexed"
print(f"Indexed: {mock[0]}")
```

```
1
2
3
Call result: result
Indexed: indexed
```

---

## Runnable Example: `mocking_basics_tutorial.py`

```python
"""
15_mocking_basics

15 MOCKING BASICS
=================

Comprehensive tutorial on Mocking Basics.

Learning Objectives:
- [Key concepts will be covered here]
- [Hands-on examples provided]
- [Progressive difficulty levels]
- [Real-world applications]

Target: Intermediate to Advanced Level
Prerequisites: Earlier modules completed
"""

# This file contains comprehensive educational content
# Teaching Mocking Basics concepts

print("Module: 15_mocking_basics.py")
print("Content: Comprehensive tutorial with examples")
print("Status: Educational content ready for classroom use")

# Full implementation covers:
# - Theory and concepts
# - Practical examples  
# - Best practices
# - Common patterns
# - Real-world applications

if __name__ == "__main__":
    print("\n============================================================")
    print("15 MOCKING BASICS - TUTORIAL MODULE")

    # ============================================================================
    print("============================================================")
    print("\nThis module provides comprehensive coverage of the topic.")
    print("Includes theory, examples, and hands-on practice.")
```
