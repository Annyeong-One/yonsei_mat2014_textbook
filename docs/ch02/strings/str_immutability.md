

# `str`: Immutability

Python strings are **immutable**: once created, their contents cannot be changed.

This means operations on strings **never modify the original object**.
Instead, they **create new strings**.

---

## Attempting to Modify a String

Trying to change a character in a string raises an error.

```python
a = "Hello Pi"

print(a[1])  # e

a[1] = "E"
# TypeError: 'str' object does not support item assignment
```

Strings do not support **item assignment**, so individual characters cannot be modified.

---

## String Methods Return New Objects

String methods return **new strings** rather than modifying the original.

```python
def main():
    s = "the brand has had its ups and downs."

    upper = s.upper()

    print(s)      # original string
    print(upper)  # new string

if __name__ == "__main__":
    main()
```

Output:

```
the brand has had its ups and downs.
THE BRAND HAS HAD ITS UPS AND DOWNS.
```

The original string remains unchanged.

---

## New Object Creation

Operations on strings produce **new objects**.

```python
a = "hello"
b = a.upper()

print(id(a))
print(id(b))
```

The object IDs differ, showing that a **new string object was created**.

---

## Variable Rebinding

Variables can be reassigned to reference new objects.

```python
a = "hello"
b = a

a = a.upper()

print(a)  # HELLO
print(b)  # hello
```

The original string still exists. The variable `a` simply points to a new object.

---

## Slicing Creates New Strings

Slicing also produces new string objects.

```python
a = "PI"

b = a[::-1]

print(a)  # PI
print(b)  # IP
```

The original string is unchanged.

---

## Why Strings Are Immutable

Immutability provides several advantages.

### Memory Efficiency

Python can reuse identical string objects.

```python
a = "hello"
b = "hello"

print(a is b)  # often True
```

This optimization is called **string interning**. Small strings may be interned by Python, but interning behavior is implementation dependent.

---

### Hashability

Immutable objects can be used as dictionary keys.

```python
d = {"hello": 1}
```

Mutable objects cannot reliably serve as keys.

---

### Thread Safety

Immutable objects can be shared safely between threads. Because the object cannot change, multiple threads can safely read the same string without synchronization.

---

### Predictability

Functions cannot accidentally modify the caller's string.

```python
def process(s):
    return s.upper()

original = "hello"
result = process(original)

print(original)  # still "hello"
```

This eliminates unintended side effects.

---

## Key Takeaways

* Python strings are **immutable**.
* Characters cannot be modified after creation.
* String methods **return new objects**.
* Variables may be reassigned, but the original object is unchanged.
* Immutability enables **memory optimizations, hashing, and safer code**.

