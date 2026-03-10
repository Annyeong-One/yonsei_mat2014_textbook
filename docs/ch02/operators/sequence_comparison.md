# Sequence Comparison


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python compares sequences (strings, lists, tuples) **lexicographically** — element by element from left to right.


## String Comparison

Strings are compared character by character using ASCII/Unicode values.

```python
print("apple" < "banana")   # True
print("apple" < "apricot")  # True (5th char: 'l' < 'r')
print("Apple" < "apple")    # True (uppercase comes first)
```

### ASCII Order

Capital letters have lower ASCII values than lowercase:

```python
print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord('a'))  # 97
print(ord('z'))  # 122
```

This means:

```python
print("Zebra" < "apple")  # True (Z=90 < a=97)
print("Girl" < "boy")     # True (G=71 < b=98)
```

**Caution**: This differs from dictionary ordering where case is typically ignored.


## List Comparison

Lists are compared element by element:

```python
print([1, 2, 3] < [1, 2, 4])  # True (3 < 4)
print([1, 2, 3] < [1, 3, 0])  # True (2 < 3, rest ignored)
print([1, 2, 3] < [2, 0, 0])  # True (1 < 2, rest ignored)
```

### First Difference Wins

```python
print([0, 1, 2] < [5, 1, 2])          # True (0 < 5)
print([0, 1, 2000000] < [0, 1, 2])    # False (2000000 > 2)
```

### String Elements

```python
print(['Jones', 'Sally'] < ['Jones', 'Fred'])  # False ('S' > 'F')
print(['Jones', 'Sally'] < ['Adams', 'Sam'])   # False ('J' > 'A')
```


## Tuple Comparison

Tuples follow the same rules as lists:

```python
print((1, 2, 3) < (1, 2, 4))  # True
print((1, 2, 3) < (1, 3, 0))  # True
print((0, 1, 2) < (5, 1, 2))  # True
```


## Comparison Algorithm

1. Compare first elements
2. If equal, compare second elements
3. Continue until a difference is found or one sequence ends
4. Shorter sequence is "less than" if all compared elements are equal

```python
print([1, 2] < [1, 2, 3])     # True (shorter)
print("ab" < "abc")           # True (shorter)
print((1, 2) == (1, 2))       # True (all equal)
```


## Chained Comparisons

Python supports chained comparisons:

```python
print(1 < 2 < 3)              # True (1<2 and 2<3)
print("a" < "b" < "c")        # True
print(1 < 2 < 3 < 4 < 5)      # True
```

This is equivalent to:

```python
print(1 < 2 and 2 < 3)        # True
```


## Mixed Type Comparison

Comparing incompatible types raises `TypeError`:

```python
# Python 3
print([1, 2] < "ab")  # TypeError: '<' not supported
print((1, 2) < [1, 2])  # TypeError
```


## Practical Use: Sorting

Lexicographic comparison enables natural sorting:

```python
names = ["Charlie", "Alice", "Bob"]
print(sorted(names))  # ['Alice', 'Bob', 'Charlie']

# Tuples sort by first element, then second
records = [("Bob", 25), ("Alice", 30), ("Bob", 20)]
print(sorted(records))  # [('Alice', 30), ('Bob', 20), ('Bob', 25)]
```


## Summary

| Sequence | Comparison Basis |
|----------|------------------|
| String | Character ASCII/Unicode values |
| List | Element-by-element comparison |
| Tuple | Element-by-element comparison |

- Comparison stops at first difference
- Shorter sequence is "less than" if prefixes match
- Case matters: `'A' < 'a'` (ASCII order)
