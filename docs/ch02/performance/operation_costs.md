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

### Four Ways to Transform a List

Python offers four common patterns for applying a function to every element. Each has different performance characteristics because of how much work stays in the interpreter versus compiled C code:

```python
import time

words = ['hello', 'world', 'python'] * 10_000

# 1. Explicit for loop with append
tic = time.time()
result = []
for word in words:
    result.append(word.upper())
loop_time = time.time() - tic

# 2. map() — pushes the loop into C
tic = time.time()
result = list(map(str.upper, words))
map_time = time.time() - tic

# 3. List comprehension
tic = time.time()
result = [w.upper() for w in words]
comp_time = time.time() - tic

# 4. Generator expression (lazy, no intermediate list)
tic = time.time()
result = list(s.upper() for s in words)
gen_time = time.time() - tic

print(f"for loop:       {loop_time:.4f}s")
print(f"map():          {map_time:.4f}s")
print(f"comprehension:  {comp_time:.4f}s")
print(f"generator:      {gen_time:.4f}s")
```

`map()` is typically fastest because the entire iteration happens in C with no per-element bytecode overhead. List comprehensions are faster than explicit loops because the append is handled internally. Generator expressions avoid allocating the full list but add per-element suspension overhead.

---

## Attribute Lookup Overhead

### Avoiding Dots in Inner Loops

Every dot (`.`) in Python triggers an attribute lookup. In tight loops over large data, caching the method reference outside the loop can produce measurable speedups:

```python
import timeit

# With dots: word.upper() resolves the method on every iteration
code_with_dot = """
oldlist = ['some', 'string', 'that', 'is', 'big'] * 50000
newlist = []
for word in oldlist:
    newlist.append(word.upper())
"""

# Without dots: pre-bind both upper and append
code_without_dot = """
oldlist = ['some', 'string', 'that', 'is', 'big'] * 50000
upper = str.upper
newlist = []
append = newlist.append
for word in oldlist:
    append(upper(word))
"""

t_dot = timeit.timeit(stmt=code_with_dot, number=10)
t_nodot = timeit.timeit(stmt=code_without_dot, number=10)

print(f"With dots:    {t_dot:.4f}s")
print(f"Without dots: {t_nodot:.4f}s")
print(f"Speedup:      {t_dot / t_nodot:.2f}x")
```

The speedup comes from eliminating two dictionary lookups per iteration: one for `newlist.append` and one for `word.upper`. For small loops the difference is negligible, but for millions of iterations it adds up. This technique is most useful in performance-critical inner loops where every microsecond matters.

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
