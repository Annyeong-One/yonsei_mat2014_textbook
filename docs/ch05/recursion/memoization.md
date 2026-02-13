# Memoization and Recursion

Memoization caches function results to avoid redundant computations. It transforms exponential-time recursive algorithms into polynomial-time solutions.

---

## The Problem: Redundant Computation

```python
def fibonacci(n):
    '''Naive fibonacci: exponential time O(2^n)'''
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci(5) calls fibonacci(3) three times, fibonacci(2) five times!
# Time complexity: O(2^n)
import time
start = time.time()
result = fibonacci(35)
elapsed = time.time() - start
print(f"fibonacci(35) = {result}, took {elapsed:.2f} seconds")
```

## lru_cache Decorator

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    '''Memoized fibonacci: linear time O(n)'''
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

# Now O(n) instead of O(2^n)!
import time
start = time.time()
result = fibonacci_cached(35)
elapsed = time.time() - start
print(f"fibonacci_cached(35) = {result}, took {elapsed:.6f} seconds")

# View cache statistics
print(fibonacci_cached.cache_info())
```

## Manual Memoization

```python
def fibonacci_memo(n, cache=None):
    '''Manual memoization with dictionary'''
    if cache is None:
        cache = {}
    
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    cache[n] = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)
    return cache[n]

print(fibonacci_memo(30))  # Nearly instant
```

## Example: Longest Common Subsequence

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def lcs(text1, text2):
    '''Longest common subsequence using memoization'''
    if not text1 or not text2:
        return 0
    
    if text1[0] == text2[0]:
        return 1 + lcs(text1[1:], text2[1:])
    
    return max(
        lcs(text1[1:], text2),
        lcs(text1, text2[1:])
    )

print(lcs("abcde", "ace"))     # 3
print(lcs.cache_info())         # Show cache hits/misses
```

## Cache Strategies

```python
from functools import lru_cache

# Limited cache size (evicts least recently used)
@lru_cache(maxsize=128)
def expensive_function(x):
    return x ** 2

# Unbounded cache (use with caution)
@lru_cache(maxsize=None)
def mathematical_function(n):
    return n * (n + 1) // 2

# Clear cache when needed
expensive_function.cache_clear()
```

## Performance Impact

Memoization provides dramatic speedup for recursive algorithms with overlapping subproblems:
- Without memoization: O(2^n)
- With memoization: O(n)
