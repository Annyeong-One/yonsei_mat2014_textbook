# Membership Operators

Membership operators test whether a value exists in a sequence (string, list, tuple, set, dict).

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `in` | Value found | `'a' in 'cat'` | `True` |
| `not in` | Value not found | `'z' not in 'cat'` | `True` |


## String Membership

Check if a substring exists:

```python
print('a' in 'cat')       # True
print('at' in 'cat')      # True
print('dog' in 'cat')     # False
print('z' not in 'cat')   # True
```


## List Membership

Check if an element exists:

```python
fruits = ['apple', 'banana', 'cherry']

print('apple' in fruits)    # True
print('grape' in fruits)    # False
print('grape' not in fruits) # True
```

### Boolean/Integer Gotcha

```python
print(True in [1])    # True (because True == 1)
print(False in [0])   # True (because False == 0)
print(True in [2])    # False
```

This happens because `True == 1` and `False == 0` in Python.


## Tuple Membership

Same as lists:

```python
colors = ('red', 'green', 'blue')

print('red' in colors)     # True
print('yellow' in colors)  # False
```


## Set Membership

Sets are optimized for membership testing (O(1)):

```python
numbers = {1, 2, 3, 4, 5}

print(3 in numbers)   # True
print(10 in numbers)  # False
```


## Dictionary Membership

By default, `in` checks **keys**:

```python
person = {'name': 'Alice', 'age': 30}

print('name' in person)     # True (key exists)
print('Alice' in person)    # False (not a key)
print('city' not in person) # True
```

### Check Values

```python
print('Alice' in person.values())  # True
```

### Check Key-Value Pairs

```python
print(('name', 'Alice') in person.items())  # True
```


## Performance Considerations

| Container | Time Complexity |
|-----------|-----------------|
| list | O(n) |
| tuple | O(n) |
| str | O(n) |
| set | O(1) average |
| dict | O(1) average |

For large collections with frequent lookups, use `set` or `dict`:

```python
# Slow for large lists
if item in large_list:  # O(n)
    ...

# Fast for sets
if item in large_set:   # O(1)
    ...
```


## Practical Examples

### Input Validation

```python
valid_options = {'yes', 'no', 'maybe'}

user_input = input("Enter choice: ").lower()
if user_input in valid_options:
    print("Valid choice")
else:
    print("Invalid choice")
```

### Filtering

```python
vowels = 'aeiou'
text = "Hello World"

# Filter vowels
result = [c for c in text.lower() if c in vowels]
print(result)  # ['e', 'o', 'o']
```

### Finding Missing Items

```python
required = {'name', 'email', 'phone'}
provided = {'name', 'email'}

missing = [field for field in required if field not in provided]
print(missing)  # ['phone']
```


## Range Membership

```python
print(5 in range(10))     # True
print(10 in range(10))    # False (exclusive end)
print(15 in range(0, 20, 5))  # True (0, 5, 10, 15)
```


## Custom Objects

Classes can define custom `in` behavior with `__contains__`:

```python
class EvenNumbers:
    def __contains__(self, n):
        return n % 2 == 0

evens = EvenNumbers()
print(4 in evens)   # True
print(5 in evens)   # False
```


## Summary

- `in` checks membership, `not in` checks absence
- Works with strings, lists, tuples, sets, dicts
- Dict membership checks **keys** by default
- Sets have O(1) lookup — use for frequent checks
- Use `__contains__` for custom membership logic
