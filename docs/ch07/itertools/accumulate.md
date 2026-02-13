# accumulate

`accumulate()` applies a function cumulatively to items, computing running totals or products.

## Cumulative Sum

Compute running totals using the default addition operation.

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

Use any function to accumulate values.

```python
from itertools import accumulate
import operator

data = [1, 2, 3, 4]

# Cumulative product
product = list(accumulate(data, operator.mul))
print("Product:", product)

# Custom max tracking
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

