# accumulate

`accumulate()` applies a function cumulatively to items, computing running totals or products. Running accumulations appear frequently in data processing tasks such as computing cumulative sums for time series, tracking running extremes, or building prefix computations. This function provides a concise, iterator-based approach to these patterns without requiring manual loop state.

## Cumulative Sum

The simplest use of `accumulate()` computes a running total. When no function argument is provided, it defaults to addition, yielding the cumulative sum at each position.

```python
from itertools import accumulate

data = [1, 2, 3, 4, 5]
result = list(accumulate(data))
print(result)
```

```
[1, 3, 6, 10, 15]
```

## Custom Accumulation Function

By passing a two-argument function as the second parameter, you can customize the accumulation operation. The function receives the accumulated value so far and the next element from the iterable.

```python
from itertools import accumulate
import operator

data = [1, 2, 3, 4]

# Cumulative product
product = list(accumulate(data, operator.mul))
print("Product:", product)

# Running maximum (using a wrapper for clarity)
def track_max(a, b):
    return max(a, b)

values = [3, 1, 5, 2, 8, 4]
max_so_far = list(accumulate(values, track_max))
print("Max so far:", max_so_far)
```

```
Product: [1, 2, 6, 24]
Max so far: [3, 3, 5, 5, 8, 8]
```
