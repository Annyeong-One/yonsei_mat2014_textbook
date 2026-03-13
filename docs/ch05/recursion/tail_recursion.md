# Tail Recursion

Tail recursion is an optimization where the recursive call is the last operation in a function. Some languages optimize tail calls, but Python doesn't support tail call optimization (TCO) by design.

---

## Tail Recursive Pattern

In a tail recursive function, the recursive call is the final operation:

```python
# Tail recursive: recursive call is the last statement
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    # The return of the recursive call is the last operation
    return factorial_tail(n - 1, n * accumulator)

print(factorial_tail(5))   # 120
print(factorial_tail(5, 1))  # 120
```

Compare with non-tail recursion:

```python
# Non-tail recursive: multiplication happens after recursive call
def factorial_non_tail(n):
    if n <= 1:
        return 1
    return n * factorial_non_tail(n - 1)  # Returns result of multiply, not recursion
```

## Why Tail Recursion Matters

In languages with TCO (Scheme, Scala, some functional languages), tail recursive functions don't grow the call stack:

```python
# Without TCO, this pattern uses O(n) stack space in any language
def count_down_tail(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    return count_down_tail(n - 1)  # Python: still uses O(n) stack

count_down_tail(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Done!
```

## Converting to Iterative (Python Best Practice)

Since Python doesn't optimize tail calls, convert tail recursive code to iteration:

```python
# Tail recursive version (uses stack)
def sum_tail_recursive(numbers, index=0, accumulator=0):
    if index >= len(numbers):
        return accumulator
    return sum_tail_recursive(numbers, index + 1, accumulator + numbers[index])

# Iterative version (better for Python)
def sum_iterative(numbers):
    accumulator = 0
    for num in numbers:
        accumulator += num
    return accumulator

numbers = [1, 2, 3, 4, 5]
print(sum_tail_recursive(numbers))  # 15
print(sum_iterative(numbers))        # 15
```

## Key Takeaway for Python

Python deliberately doesn't support TCO. When you identify tail recursive code:
1. Convert to iteration for better performance
2. Or use accumulator pattern if recursion is clearer
3. Accept the O(n) stack space usage if recursion adds clarity
