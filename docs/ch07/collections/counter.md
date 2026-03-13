# Counter

A `Counter` is a dict subclass designed for counting hashable objects. It's the Pythonic way to do frequency analysis.

---

## Creating Counters

```python
from collections import Counter

# From string
c = Counter('mississippi')
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# From list
c = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
# Counter({'blue': 3, 'red': 2, 'green': 1})

# From dict
c = Counter({'a': 4, 'b': 2})

# From keyword arguments
c = Counter(cats=4, dogs=2)
```

---

## Accessing Counts

```python
c = Counter('mississippi')

c['i']              # 4
c['s']              # 4
c['x']              # 0 (no KeyError!)
```

**Key difference from dict**: Missing keys return `0`, not `KeyError`.

---

## most_common()

Get elements sorted by frequency:

```python
c = Counter('mississippi')

c.most_common()     # [('i', 4), ('s', 4), ('p', 2), ('m', 1)]
c.most_common(2)    # [('i', 4), ('s', 4)] (top 2)
c.most_common()[:-3:-1]  # [('m', 1), ('p', 2)] (bottom 2)
```

---

## Updating Counts

### Add Counts

```python
c = Counter(a=3, b=1)
c.update({'a': 1, 'c': 2})
print(c)  # Counter({'a': 4, 'c': 2, 'b': 1})

c.update('aaa')  # From iterable
print(c)  # Counter({'a': 7, 'c': 2, 'b': 1})
```

### Subtract Counts

```python
c = Counter(a=4, b=2, c=0)
c.subtract({'a': 1, 'b': 3})
print(c)  # Counter({'a': 3, 'c': 0, 'b': -1})
```

**Note**: `subtract()` can result in negative counts.

---

## Counter Arithmetic

```python
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

# Addition
c1 + c2             # Counter({'a': 4, 'b': 3})

# Subtraction (keeps positive only)
c1 - c2             # Counter({'a': 2})

# Intersection (min of each)
c1 & c2             # Counter({'a': 1, 'b': 1})

# Union (max of each)
c1 | c2             # Counter({'a': 3, 'b': 2})
```

---

## elements()

Returns an iterator over elements, repeating each by its count:

```python
c = Counter(a=3, b=2, c=1)
list(c.elements())  # ['a', 'a', 'a', 'b', 'b', 'c']

# Negative counts are ignored
c = Counter(a=2, b=-1)
list(c.elements())  # ['a', 'a']
```

---

## total() (Python 3.10+)

Sum of all counts:

```python
c = Counter(a=3, b=2, c=1)
c.total()           # 6
```

For earlier Python versions:

```python
sum(c.values())     # 6
```

---

## Practical Examples

### Word Frequency

```python
from collections import Counter

text = "the quick brown fox jumps over the lazy dog the fox"
words = text.lower().split()
word_counts = Counter(words)

print(word_counts.most_common(3))
# [('the', 3), ('fox', 2), ('quick', 1)]
```

### Character Frequency

```python
text = "Hello World"
char_counts = Counter(text.lower())
print(char_counts)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

### Finding Duplicates

```python
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
counts = Counter(items)

duplicates = [item for item, count in counts.items() if count > 1]
print(duplicates)  # ['apple', 'banana']
```

### Anagram Check

```python
def is_anagram(s1, s2):
    return Counter(s1.lower().replace(' ', '')) == Counter(s2.lower().replace(' ', ''))

print(is_anagram('listen', 'silent'))  # True
print(is_anagram('hello', 'world'))    # False
```

### Inventory Management

```python
inventory = Counter(apples=10, oranges=5, bananas=8)

# Sell items
sold = Counter(apples=3, oranges=2)
inventory.subtract(sold)
print(inventory)  # Counter({'bananas': 8, 'apples': 7, 'oranges': 3})

# Restock
restock = Counter(apples=5, grapes=10)
inventory.update(restock)
print(inventory)
# Counter({'apples': 12, 'grapes': 10, 'bananas': 8, 'oranges': 3})
```

### Vote Counting

```python
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob']
results = Counter(votes)

winner = results.most_common(1)[0]
print(f"Winner: {winner[0]} with {winner[1]} votes")
# Winner: Alice with 3 votes
```

---

## Counter vs defaultdict(int)

| Feature | `Counter` | `defaultdict(int)` |
|---------|-----------|-------------------|
| Missing key | Returns 0 | Returns 0 |
| `most_common()` | ✅ Yes | ❌ No |
| Arithmetic (`+`, `-`) | ✅ Yes | ❌ No |
| `elements()` | ✅ Yes | ❌ No |
| `subtract()` | ✅ Yes | ❌ No |

**Use `Counter`** for counting tasks. Use `defaultdict(int)` only if you need dict-specific behavior.

---

## Key Takeaways

- `Counter` is optimized for counting hashable objects
- Missing keys return `0` (no KeyError)
- `most_common(n)` returns top n elements
- Supports arithmetic: `+`, `-`, `&`, `|`
- `elements()` iterates with repetition
- Perfect for frequency analysis, anagrams, voting, inventory
