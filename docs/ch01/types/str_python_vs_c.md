# `str`: Python vs C

Python strings (`str`) differ dramatically from C strings in safety, semantics, and usability.

---

## C strings

In C:
- strings are arrays of characters
- terminated by a null byte (`\0`)
- no built-in length tracking

This leads to:
- buffer overflows
- undefined behavior

---

## Python strings

Python `str`:
- is an immutable object
- stores length explicitly
- supports Unicode by default

```python
s = "finance"
len(s)   # 7
```

---

## Immutability

Strings cannot be modified in place:

```python
s = "abc"
# s[0] = "A" # error
s = "A" + s[1:]
```

Immutability enables:
- safety
- hashing
- efficient reuse

---

## Unicode support

Python strings handle Unicode naturally:

```python
s = "π ≈ 3.14"
```

This is essential for internationalization and modern text processing.

---

## Key takeaways

- Python strings are safe and Unicode-aware.
- They are immutable objects.
- Very different from C strings in semantics.
