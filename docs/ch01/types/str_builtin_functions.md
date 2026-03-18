

# str Built-in Functions

Several built-in functions work naturally with strings.

These functions help inspect, transform, and analyze text.

Common examples include:

- `len()`
- `str()`
- `sorted()`
- `reversed()`
- `enumerate()`
- `ord()`
- `chr()`

```mermaid
flowchart TD
    A[Built-ins for strings]
    A --> B[len]
    A --> C[sorted]
    A --> D[reversed]
    A --> E[enumerate]
    A --> F[ord/chr]
````

---

## 1. len()

Returns the number of characters in a string.

```python
text = "Python"
print(len(text))
```

Output:

```text
6
```

---

## 2. str()

Converts values to strings.

```python
x = 42
print(str(x))
```

Output:

```text
42
```

---

## 3. sorted()

Returns a sorted list of characters.

```python
text = "cab"
print(sorted(text))
```

Output:

```text
['a', 'b', 'c']
```

---

## 4. reversed()

Returns characters in reverse order.

```python
text = "abc"
print(list(reversed(text)))
```

Output:

```text
['c', 'b', 'a']
```

---

## 5. enumerate()

Pairs indexes with characters.

```python
for i, ch in enumerate("cat"):
    print(i, ch)
```

Output:

```text
0 c
1 a
2 t
```

---

## 6. ord() and chr()

`ord()` converts a character to its Unicode code point.

`chr()` converts a code point back to a character.

```python
print(ord("A"))
print(chr(65))
```

Output:

```text
65
A
```

---

## 7. Worked Examples

### Example 1: count letters using len

```python
word = "banana"
print(len(word))
```

### Example 2: alphabetical characters

```python
print(sorted("python"))
```

### Example 3: character code

```python
print(ord("z"))
```

---

## 8. Summary

Key ideas:

* many built-ins work naturally with strings
* `len()` measures strings
* `sorted()` and `reversed()` operate on characters
* `enumerate()` pairs indexes with characters
* `ord()` and `chr()` connect characters to Unicode integers

Built-in functions complement string methods and expand what can be done with text.