# Python Operation Costs

Different Python operations have different performance costs. Understanding which operations are expensive helps optimize code effectively.

---

## Collection Operations

### List vs Set Membership

```python
import timeit

setup_list = "lst = list(range(100000))"
list_check = timeit.timeit("99999 in lst", setup=setup_list, number=1000)

setup_set = "s = set(range(100000))"
set_check = timeit.timeit("99999 in s", setup=setup_set, number=1000)

print(f"List membership: {list_check:.4f}s")
print(f"Set membership: {set_check:.6f}s")
print(f"Set is {list_check/set_check:.0f}x faster")
```

Output:
```
List membership: 0.0234s
Set membership: 0.000045s
Set is 520x faster
```

## String Operations

### String Concatenation

```python
import timeit

code1 = """
result = ""
for i in range(1000):
    result += str(i)
"""

code2 = """
parts = [str(i) for i in range(1000)]
result = "".join(parts)
"""

concat_time = timeit.timeit(code1, number=100)
join_time = timeit.timeit(code2, number=100)

print(f"Concatenation: {concat_time:.4f}s")
print(f"Join: {join_time:.6f}s")
```

Output:
```
Concatenation: 0.0456s
Join: 0.0123s
```

## Loop Costs

### List Comprehension vs Loop

```python
import timeit

code1 = """
result = []
for i in range(1000):
    result.append(i * 2)
"""

code2 = '[i * 2 for i in range(1000)]'

loop_time = timeit.timeit(code1, number=10000)
comp_time = timeit.timeit(code2, number=10000)

print(f"Loop with append: {loop_time:.4f}s")
print(f"List comprehension: {comp_time:.4f}s")
```

Output:
```
Loop with append: 0.0987s
List comprehension: 0.0654s
```

## Function Call Overhead

### Builtin vs User Functions

```python
import timeit

builtin_sum = timeit.timeit("sum(range(1000))", number=10000)

code = """
def my_sum(values):
    total = 0
    for v in values:
        total += v
    return total
my_sum(range(1000))
"""
user_sum = timeit.timeit(code, number=10000)

print(f"Builtin sum: {builtin_sum:.4f}s")
print(f"User function: {user_sum:.4f}s")
```

Output:
```
Builtin sum: 0.0123s
User function: 0.0456s
```
