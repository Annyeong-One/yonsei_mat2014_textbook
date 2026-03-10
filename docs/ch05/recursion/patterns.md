# Recursion Patterns


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Types of Recursion

### 1. Direct Recursion

A function calls itself directly.

```
f → f → f → base case
```

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # Direct call to itself

print(factorial(5))  # 120
```

### 2. Indirect Recursion

Functions call each other in a cycle.

```
f → g → f → g → base case
```

```python
n = 1

def print_odd():
    global n
    if n <= 10:
        print(n + 1, end=" ")
        n += 1
        print_even()

def print_even():
    global n
    if n <= 10:
        print(n - 1, end=" ")
        n += 1
        print_odd()

print_odd()  # 2 1 4 3 6 5 8 7 10 9
```


## Tail vs Non-Tail Recursion

### 1. Tail Recursion

The recursive call is the **last operation** — nothing happens after it returns.

```python
def countdown(n):
    if n == 0:
        return
    print(n, end=" ")
    return countdown(n - 1)  # Last operation

countdown(3)  # 3 2 1
```

### 2. Non-Tail Recursion

Operations occur **after** the recursive call returns.

```python
def countdown_reverse(n):
    if n == 0:
        return
    countdown_reverse(n - 1)  # Not the last operation
    print(n, end=" ")         # This happens after

countdown_reverse(3)  # 1 2 3
```

### 3. Why It Matters

Tail recursion can theoretically be optimized to use constant stack space (tail call optimization). However, **Python does not implement TCO**, so both forms use O(n) stack space.

```python
# Tail recursive factorial
def factorial_tail(n, acc=1):
    if n <= 1:
        return acc
    return factorial_tail(n - 1, n * acc)

# Still causes stack overflow for large n in Python
```


## Fibonacci: A Case Study

The Fibonacci sequence demonstrates different recursion strategies.

$$F(n) = F(n-1) + F(n-2), \quad F(0)=0, \quad F(1)=1$$

### 1. Naïve Recursion — O(2^n)

```python
def fib_naive(n):
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)
```

**Problem**: Exponential time due to repeated calculations.

```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   └── fib(1)
│   └── fib(2)
└── fib(3)
    ├── fib(2)
    └── fib(1)
```

Time complexity: $T(n) \in \Theta(\phi^n)$ where $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$

### 2. Memoization (Top-Down) — O(n)

Cache results to avoid redundant calculations.

```python
memo = {0: 0, 1: 1}

def fib_memo(n):
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

print(fib_memo(50))  # 12586269025
```

Or using `@lru_cache`:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)
```

- Time: O(n)
- Space: O(n) for cache + O(n) for call stack

### 3. Tabulation (Bottom-Up) — O(n) time, O(1) space

Build solution iteratively from base cases.

```python
def fib_iterative(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

print(fib_iterative(50))  # 12586269025
```

- Time: O(n)
- Space: O(1)
- No recursion stack

### 4. Binet's Formula — O(1)

Closed-form solution using the golden ratio.

$$F(n) = \frac{\phi^n - (-\phi)^{-n}}{\sqrt{5}}, \quad \phi = \frac{1+\sqrt{5}}{2}$$

```python
import math

def fib_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-phi)**(-n)) / math.sqrt(5))

print(fib_binet(50))  # 12586269025
```

**Caveat**: Floating-point errors make this inaccurate for large n.


## Complexity Comparison

| Method | Time | Space | Stack Depth | Best For |
|--------|------|-------|-------------|----------|
| Naïve Recursion | O(2^n) | O(n) | Deep | Education only |
| Memoization | O(n) | O(n) | Moderate | When recursion preferred |
| Tabulation | O(n) | O(1) | None | Production use |
| Binet's Formula | O(1) | O(1) | None | Approximation only |


## Classic Recursive Problems

### 1. Sum to N

```python
def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)

print(sum_to_n(10))  # 55
```

### 2. Triangular Numbers

$$T_n = T_{n-1} + n, \quad T_1 = 1$$

```python
def triangular(n):
    if n == 1:
        return 1
    return triangular(n - 1) + n

for i in range(1, 7):
    print(f"T_{i} = {triangular(i)}")
# T_1 = 1, T_2 = 3, T_3 = 6, T_4 = 10, T_5 = 15, T_6 = 21
```

### 3. Tower of Hanoi

$$a_n = 2a_{n-1} + 1, \quad a_1 = 1$$

Minimum moves to solve n-disk puzzle.

```python
def hanoi_moves(n):
    if n == 1:
        return 1
    return 2 * hanoi_moves(n - 1) + 1

for i in range(1, 8):
    print(f"n={i}: {hanoi_moves(i)} moves")
# n=1: 1, n=2: 3, n=3: 7, n=4: 15, n=5: 31, n=6: 63, n=7: 127
```


## Advantages and Disadvantages

### Advantages

1. **Elegant code** — Natural expression for recursive problems
2. **Divide-and-conquer** — Breaks complex problems into subproblems
3. **Tree structures** — Natural fit for trees and graphs

### Disadvantages

1. **Stack overhead** — Each call adds a frame
2. **Performance** — Function call overhead vs iteration
3. **Stack overflow** — Deep recursion hits Python's limit
4. **Debugging** — Harder to trace execution flow


## When to Use Recursion

**Use recursion when:**

- Problem has recursive structure (trees, graphs)
- Divide-and-conquer is natural
- Code clarity matters more than performance
- Depth is bounded and manageable

**Use iteration when:**

- Simple loops suffice
- Performance is critical
- Deep recursion is possible
- Stack overflow is a concern


## Summary

- **Direct recursion**: Function calls itself
- **Indirect recursion**: Functions call each other cyclically
- **Tail recursion**: Recursive call is last operation (no TCO in Python)
- **Memoization**: Top-down DP, caches results
- **Tabulation**: Bottom-up DP, iterative
- **Trade-off**: Recursion for clarity, iteration for performance
