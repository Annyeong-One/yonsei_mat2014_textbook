# Common Runtime Errors

Python raises exceptions when something goes wrong at runtime. Recognizing common errors helps you debug quickly.

---

## 1. `TypeError`

Raised when an operation is applied to an inappropriate type.

```python
"1" + 2
```

---

## 2. `ValueError`

Raised when a function receives the right type but an invalid value.

```python
int("abc")
```

---

## 3. `IndexError`

Raised when accessing an invalid index in a sequence.

```python
xs = [1, 2]
xs[10]
```

---

## 4. `KeyError`

Raised when a dictionary key is missing.

```python
d = {}
d["x"]
```

---

## 5. `ZeroDivisionError`

Raised when dividing by zero.

```python
1 / 0
```

---

## Key takeaways

- Errors are explicit, not silent.
- Exception messages guide debugging.
- Learn to recognize common exceptions.
