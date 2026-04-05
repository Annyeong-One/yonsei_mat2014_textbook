
# sorted() and reversed()

These built-ins manipulate sequence order.

```mermaid
flowchart TD
    A[Sequence]
    A --> B[sorted()]
    A --> C[reversed()]
````

---

## sorted()

Returns a **new sorted list**.

```python
numbers = [3,1,4,2]

print(sorted(numbers))
```

Output

```
[1,2,3,4]
```

Descending order

```python
print(sorted(numbers, reverse=True))
```

---

## Sorting Strings

```python
names = ["Charlie","Alice","Bob"]

print(sorted(names))
```

Output

```
['Alice','Bob','Charlie']
```

---

## reversed()

Returns elements in reverse order.

```python
numbers = [1,2,3]

for n in reversed(numbers):
    print(n)
```

Output

```
3
2
1
```

---

## Exercises

**Exercise 1.**
`sorted()` returns a new list, while `list.sort()` sorts in place. Predict the output:

```python
a = [3, 1, 2]
b = sorted(a)
c = a.sort()
print(a)
print(b)
print(c)
```

Why does `c` contain `None`? What is the fundamental design difference between `sorted()` and `.sort()`, and when should you use each?

??? success "Solution to Exercise 1"
    Output:

    ```text
    [1, 2, 3]
    [1, 2, 3]
    None
    ```

    `sorted(a)` creates and returns a **new sorted list**, leaving `a` unchanged -- but then `a.sort()` sorts `a` **in place** and returns `None`.

    `c` is `None` because `.sort()` returns `None` by convention -- it modifies the list in place rather than creating a new one. This is Python's convention for mutating methods: they return `None` to signal that the operation was in-place.

    Use `sorted()` when you need the original order preserved or when working with immutable sequences (tuples, strings). Use `.sort()` when you want to sort a list in place to save memory.

---

**Exercise 2.**
`sorted()` accepts a `key` function. Predict the output:

```python
words = ["banana", "Apple", "cherry"]
print(sorted(words))
print(sorted(words, key=str.lower))
print(sorted(words, key=len))
```

Why do the three sorts produce different orders? What does the `key` function do -- does it modify the elements or just affect comparison?

??? success "Solution to Exercise 2"
    Output:

    ```text
    ['Apple', 'banana', 'cherry']
    ['Apple', 'banana', 'cherry']
    ['Apple', 'banana', 'cherry']
    ```

    Wait -- let me recalculate. `sorted(words)` sorts by default Unicode order: `"A"` (65) < `"b"` (98) < `"c"` (99), so `['Apple', 'banana', 'cherry']`.

    `sorted(words, key=str.lower)` compares `"apple"`, `"banana"`, `"cherry"` (lowercase versions), giving alphabetical order: `['Apple', 'banana', 'cherry']`. Same result here because Apple already sorts first.

    `sorted(words, key=len)` compares lengths: `len("Apple")=5`, `len("banana")=6`, `len("cherry")=6`, so `['Apple', 'banana', 'cherry']` (stable sort preserves original order for equal lengths).

    The `key` function does NOT modify the elements -- it only produces comparison keys. The original elements appear in the output.

---

**Exercise 3.**
`reversed()` returns an iterator, not a list. Predict the output:

```python
r = reversed([1, 2, 3])
print(type(r))
print(list(r))
print(list(r))
```

Why is the second `list(r)` empty? How does `reversed()` differ from slicing with `[::-1]` in terms of memory usage and return type?

??? success "Solution to Exercise 3"
    Output:

    ```text
    <class 'list_reverseiterator'>
    [3, 2, 1]
    []
    ```

    `reversed()` returns a **lazy iterator** that can only be consumed once. The first `list(r)` exhausts the iterator. The second `list(r)` gets an empty iterator.

    `reversed()` vs `[::-1]`:
    - `reversed([1, 2, 3])` creates an iterator that produces elements in reverse order **without copying the list**. Memory usage: O(1).
    - `[1, 2, 3][::-1]` creates a **new list** with all elements in reverse. Memory usage: O(n).

    For simply iterating in reverse, `reversed()` is more memory-efficient. For getting a reversed list to keep around, `[::-1]` is more convenient.
