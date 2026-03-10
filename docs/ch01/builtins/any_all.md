# any() and all()


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

The any() and all() functions perform logical aggregation on iterables. any() returns True if at least one element is truthy, while all() returns True only if all elements are truthy. Both short-circuit, stopping evaluation early when the result is determined.

---

## any() Function

### Basic Usage

```python
print(any([False, False, True, False]))
print(any([False, False, False]))
print(any([]))
```

Output:
```
True
False
False
```

### With Generators

```python
numbers = [2, 4, 6, 8, 9]
has_odd = any(n % 2 == 1 for n in numbers)
print(f"Has odd number: {has_odd}")
```

Output:
```
Has odd number: True
```

### Checking for Valid Values

```python
user_data = {"email": "", "phone": "555-1234", "fax": ""}
has_contact = any([user_data["email"], user_data["phone"], user_data["fax"]])
print(f"Has contact info: {has_contact}")
```

Output:
```
Has contact info: True
```

## all() Function

### Validating All Elements

```python
print(all([True, True, True]))
print(all([True, False, True]))
print(all([]))
```

Output:
```
True
False
True
```

### Data Validation

```python
ages = [25, 30, 35, 40]
valid = all(age >= 18 for age in ages)
print(f"All adults: {valid}")
```

Output:
```
All adults: True
```

### Checking Conditions

```python
scores = [85, 92, 88, 76, 91]
passed = all(score >= 70 for score in scores)
print(f"All students passed: {passed}")
```

Output:
```
All students passed: True
```

## Practical Applications

### Form Validation

```python
def validate_form(form_data):
    required_fields = ["username", "email", "password"]
    all_present = all(form_data.get(field) for field in required_fields)
    return all_present

data1 = {"username": "john", "email": "john@example.com", "password": "secret"}
data2 = {"username": "jane", "email": "", "password": "secret"}

print(f"Form 1 valid: {validate_form(data1)}")
print(f"Form 2 valid: {validate_form(data2)}")
```

Output:
```
Form 1 valid: True
Form 2 valid: False
```

### Checking Range Constraints

```python
values = [5, 10, 15, 20, 25]
in_range = all(0 <= v <= 100 for v in values)
print(f"All values in range [0, 100]: {in_range}")
```

Output:
```
All values in range [0, 100]: True
```
