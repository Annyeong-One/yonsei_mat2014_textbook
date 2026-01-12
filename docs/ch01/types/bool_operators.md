# Boolean Operators

Python provides logical and bitwise operators for boolean algebra and binary operations.

---

## Logical Operators

Three primary operators for boolean logic.

### 1. and Operator

Returns `True` if both operands evaluate to `True`.

| Expression | Result |
|------------|--------|
| `True and True` | `True` |
| `True and False` | `False` |
| `False and True` | `False` |
| `False and False` | `False` |

```python
def main():
    print(True and True)
    print(True and False)
    print(False and True)
    print(False and False)

if __name__ == "__main__":
    main()
```

### 2. or Operator

Returns `True` if at least one operand evaluates to `True`.

| Expression | Result |
|------------|--------|
| `True or True` | `True` |
| `True or False` | `True` |
| `False or True` | `True` |
| `False or False` | `False` |

```python
def main():
    print(True or True)
    print(True or False)
    print(False or True)
    print(False or False)

if __name__ == "__main__":
    main()
```

### 3. not Operator

Returns the logical negation of the operand.

| Expression | Result |
|------------|--------|
| `not True` | `False` |
| `not False` | `True` |

```python
def main():
    print(not True)
    print(not False)

if __name__ == "__main__":
    main()
```

### 4. Combined Example

```python
x, y = True, False
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False
```

### 5. Hardware Logic

CPU는 집에서 만들지말고 사서쓰세요 제발 [kor](https://www.youtube.com/watch?v=WGKHEIpXy5c)

---

## Short-Circuit

Python uses short-circuit evaluation for efficiency.

### 1. and Short-Circuit

The `and` operator stops upon encountering `False`.

```python
def expensive_operation():
    print("Executing computation")
    return True

print(False and expensive_operation())  # Output: False (function not executed)
```

### 2. or Short-Circuit

The `or` operator stops upon encountering `True`.

```python
def expensive_operation():
    print("Executing computation")
    return True

print(True or expensive_operation())    # Output: True (function not executed)
```

### 3. Comparison Chain

What is the output?

```python
def three(): print("three"); return 3
def five(): print("five"); return 5
def seven(): print("seven"); return 7

def main():
    three() > five() > seven()

if __name__ == "__main__":
    main()
```

**Solution:**

```python
def three(): print("three"); return 3
def five(): print("five"); return 5
def seven(): print("seven"); return 7

def main():
    three() > five() > seven()

if __name__ == "__main__":
    main()
```

### 4. Interview Process

What is the output?

```python
def doc_screening(): print("1 doc screening"); return True
def coding_test(): print("2 coding test"); return True
def job_interview_1(): print("3 job interview 1"); return True
def job_interview_2(): print("4 job interview 2"); return False
def physical_exam(): print("5 physical exam"); return True

def main():
    if doc_screening() and coding_test() and job_interview_1() and job_interview_2() and physical_exam():
        print("Congratulation! You are now in our team.")
    else:
        print("We are sorry to inform that we cannot offer you a position at this time.")

if __name__ == "__main__":
    main()
```

**Solution:**

```python
def doc_screening(): print("1 doc screening"); return True
def coding_test(): print("2 coding test"); return True
def job_interview_1(): print("3 job interview 1"); return True
def job_interview_2(): print("4 job interview 2"); return False
def physical_exam(): print("5 physical exam"); return True

def main():
    if doc_screening() and coding_test() and job_interview_1() and job_interview_2() and physical_exam():
        print("Congratulation! You are now in our team.")
    else:
        print("We are sorry to inform that we cannot offer you a position at this time.")

if __name__ == "__main__":
    main()
```

### 5. First Operand

```python
a = True or "WOW"
print(a)

a = 1 or "WOW"
print(a)

a = 3.14 or "WOW"
print(a)

a = [1,2,3] or "WOW"
print(a)

a = (1,2,3) or "WOW"
print(a)

a = {1,2,3} or "WOW"
print(a)

a = {1:1,2:2,3:3} or "WOW"
print(a)
```

### 6. Second Operand

```python
a = False or "WOW"
print(a)

a = 0 or "WOW"
print(a)

a = 0.0 or "WOW"
print(a)

a = [] or "WOW"
print(a)

a = tuple() or "WOW"
print(a)

a = set() or "WOW"
print(a)

a = {} or "WOW"
print(a)
```

---

## Bitwise Operators

Operate at the binary level for low-level computations.

### 1. Bitwise AND (&)

```python
print(True & False)  # Output: False
print(4 & 5)  # Binary: 100 & 101 = 100 (4)
```

### 2. Bitwise OR (|)

```python
print(True | False)  # Output: True
print(4 | 5)  # Binary: 100 | 101 = 101 (5)
```

### 3. Bitwise XOR (^)

```python
print(True ^ False)  # Output: True
print(4 ^ 5)  # Binary: 100 ^ 101 = 001 (1)
```

### 4. Comparison Table

| Operator | Description | Example |
|----------|------------|---------|
| `&` | Bitwise AND | `True & False` → `False` |
| `\|` | Bitwise OR | `True \| False` → `True` |
| `^` | Bitwise XOR | `True ^ True` → `False` |

---

## Conclusion

Logical operators enable efficient boolean computations with short-circuit evaluation, while bitwise operators provide low-level binary manipulation for specialized applications like cryptography and embedded systems.
