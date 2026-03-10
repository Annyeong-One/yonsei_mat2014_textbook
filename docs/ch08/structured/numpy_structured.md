# Structured Arrays


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Structured arrays (also called record arrays) allow you to store heterogeneous data types in a single array, similar to a database table or spreadsheet row.

```python
import numpy as np
```

---

## What are Structured Arrays?

Regular NumPy arrays hold homogeneous data (all same type). Structured arrays hold **records** with multiple named fields of different types:

```python
# Regular array: all floats
regular = np.array([1.0, 2.0, 3.0])

# Structured array: mixed types
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('score', 'f8')])
structured = np.array([
    ('Alice', 25, 95.5),
    ('Bob', 30, 87.3),
    ('Charlie', 22, 91.0)
], dtype=dt)
```

---

## Creating Structured Arrays

### Method 1: dtype with List of Tuples

```python
# Define dtype: (field_name, data_type)
dt = np.dtype([
    ('name', 'U20'),    # Unicode string, max 20 chars
    ('age', 'i4'),      # 32-bit integer
    ('salary', 'f8'),   # 64-bit float
    ('active', '?')     # Boolean
])

# Create array
employees = np.array([
    ('Alice', 30, 75000.0, True),
    ('Bob', 25, 65000.0, True),
    ('Charlie', 35, 85000.0, False)
], dtype=dt)
```

### Method 2: Dictionary Format

```python
dt = np.dtype({
    'names': ['x', 'y', 'z'],
    'formats': ['f8', 'f8', 'f8']
})

points = np.array([(1.0, 2.0, 3.0), (4.0, 5.0, 6.0)], dtype=dt)
```

### Method 3: String Format

```python
# Comma-separated type strings
dt = np.dtype('U10, i4, f8')  # Unnamed fields: f0, f1, f2

data = np.array([('Alice', 25, 95.5)], dtype=dt)
print(data['f0'])  # 'Alice'
```

---

## Data Type Codes

| Code | Type | Example |
|------|------|---------|
| `'i4'` | 32-bit int | `np.int32` |
| `'i8'` | 64-bit int | `np.int64` |
| `'f4'` | 32-bit float | `np.float32` |
| `'f8'` | 64-bit float | `np.float64` |
| `'U10'` | Unicode string (10 chars) | |
| `'S10'` | Byte string (10 bytes) | |
| `'?'` | Boolean | `np.bool_` |
| `'c16'` | Complex 128 | `np.complex128` |

---

## Accessing Data

### By Field Name

```python
dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('score', 'f8')])
students = np.array([
    ('Alice', 20, 95.5),
    ('Bob', 22, 87.3),
    ('Charlie', 21, 91.0)
], dtype=dt)

# Access entire column
print(students['name'])   # ['Alice' 'Bob' 'Charlie']
print(students['age'])    # [20 22 21]
print(students['score'])  # [95.5 87.3 91. ]

# Access single record
print(students[0])        # ('Alice', 20, 95.5)
print(students[0]['name'])  # 'Alice'
```

### By Index

```python
# First record
print(students[0])  # ('Alice', 20, 95.5)

# Slice
print(students[:2])  # First two records

# Boolean indexing
adults = students[students['age'] >= 21]
print(adults['name'])  # ['Bob' 'Charlie']
```

### Multiple Fields

```python
# Select multiple fields (returns structured array)
subset = students[['name', 'score']]
print(subset.dtype)  # [('name', '<U10'), ('score', '<f8')]
```

---

## Modifying Data

```python
# Modify single field
students['score'][0] = 98.0

# Modify entire record
students[1] = ('Robert', 23, 90.0)

# Modify column
students['age'] = students['age'] + 1  # Everyone ages by 1
```

---

## Nested Structures

```python
# Nested dtype
address_dt = np.dtype([('city', 'U20'), ('zip', 'U10')])
person_dt = np.dtype([
    ('name', 'U20'),
    ('address', address_dt)
])

people = np.array([
    ('Alice', ('New York', '10001')),
    ('Bob', ('Los Angeles', '90001'))
], dtype=person_dt)

# Access nested fields
print(people['address']['city'])  # ['New York' 'Los Angeles']
```

---

## Array Fields

```python
# Field that is itself an array
dt = np.dtype([
    ('name', 'U10'),
    ('grades', 'f8', (3,))  # Array of 3 floats
])

students = np.array([
    ('Alice', [95, 87, 92]),
    ('Bob', [88, 91, 85])
], dtype=dt)

print(students['grades'])
# [[95. 87. 92.]
#  [88. 91. 85.]]

print(students[0]['grades'].mean())  # 91.33
```

---

## Record Arrays (recarray)

Record arrays allow attribute-style access:

```python
# Convert structured array to recarray
rec = students.view(np.recarray)

# Attribute access (instead of indexing)
print(rec.name)   # ['Alice' 'Bob']
print(rec.age)    # [20 22]
print(rec[0].name)  # 'Alice'

# Create recarray directly
rec = np.rec.array([
    ('Alice', 25, 95.5),
    ('Bob', 30, 87.3)
], dtype=[('name', 'U10'), ('age', 'i4'), ('score', 'f8')])
```

---

## Practical Examples

### CSV-like Data

```python
# Load CSV-like data
dt = np.dtype([
    ('id', 'i4'),
    ('product', 'U30'),
    ('price', 'f8'),
    ('quantity', 'i4')
])

inventory = np.array([
    (1, 'Widget', 9.99, 100),
    (2, 'Gadget', 24.99, 50),
    (3, 'Gizmo', 14.99, 75)
], dtype=dt)

# Calculate total value
total_value = (inventory['price'] * inventory['quantity']).sum()
print(f"Total inventory value: ${total_value:.2f}")
```

### Sorting Structured Arrays

```python
# Sort by single field
sorted_by_score = np.sort(students, order='score')

# Sort by multiple fields
sorted_multi = np.sort(students, order=['age', 'score'])
```

### Filtering

```python
# Boolean filtering
high_scorers = students[students['score'] > 90]
young_students = students[students['age'] < 22]

# Combined conditions
filtered = students[(students['age'] >= 20) & (students['score'] > 85)]
```

---

## When to Use Structured Arrays

### Use Structured Arrays When:

- Working with large datasets in pure NumPy
- Need memory-efficient storage
- Interfacing with C/binary data formats
- Simple tabular operations without pandas overhead

### Use Pandas Instead When:

- Need advanced data manipulation
- Working with time series
- Need missing value handling (NaN)
- Complex groupby/merge operations

---

## Summary

| Task | Code |
|------|------|
| Create dtype | `np.dtype([('name', 'U10'), ('age', 'i4')])` |
| Create array | `np.array([('Alice', 25)], dtype=dt)` |
| Access field | `arr['name']` |
| Access record | `arr[0]` |
| Access nested | `arr['address']['city']` |
| Sort by field | `np.sort(arr, order='age')` |
| Filter | `arr[arr['age'] > 20]` |
| To recarray | `arr.view(np.recarray)` |

**Key Takeaways**:

- Structured arrays store heterogeneous data with named fields
- Access fields by name: `arr['fieldname']`
- Use dtype codes: `'i4'` (int32), `'f8'` (float64), `'U10'` (string)
- Record arrays add attribute-style access: `arr.name`
- Can nest structures and include array fields
- Good for memory-efficient tabular data without pandas
- Use `order` parameter for sorting by fields
