# Number Systems


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python supports multiple number system representations for integers.

---

## Representations

Four different ways to represent integers in Python.

### 1. Representation Table

||Format Specifier|Key Word|Example|
|:---|:---:|:---|:---|
|Decimal (10)|d||10|
|Binary (2)|b|0b or 0B|0b10 or 0B10|
|Octal (8)|o|0o or 0O|0o10 or 0O10|
|Hexadecimal (16)|x or X|0x or 0X|0x10 or 0X10|

---

## Decimal

Decimal is the default representation (base 10).

### 1. Decimal Example

```python
def main():
    a = 10
    print(a, type(a))
    print(f"{a = }")
    print(f"{a = :d}") # Decimal Representation
    print(f"{a = :b}") # Binary Representation
    print(f"{a = :o}") # Octal Representation
    print(f"{a = :x}") # Hexadecimal Representation

if __name__ == "__main__":
    main()
```

---

## Binary

Binary representation uses base 2 with prefix `0b` or `0B`.

### 1. Binary Literals

```python
def main():
    a = 0b10
    print(a, type(a))
    print(f"{a = }")
    print(f"{a = :d}") # Decimal Representation
    print(f"{a = :b}") # Binary Representation
    print(f"{a = :o}") # Octal Representation
    print(f"{a = :x}") # Hexadecimal Representation

if __name__ == "__main__":
    main()
```

### 2. Capital Prefix

```python
def main():
    a = 0B10
    print(a, type(a))
    print(f"{a = }")
    print(f"{a = :d}") # Decimal Representation
    print(f"{a = :b}") # Binary Representation
    print(f"{a = :o}") # Octal Representation
    print(f"{a = :x}") # Hexadecimal Representation

if __name__ == "__main__":
    main()
```

### 3. Decimal to Binary

```python
def main():
    a = 17

    b = bin(a)
    print(b, type(b))  # Output: 0b10001 <class 'str'>

    c = format(a,"b")
    print(c, type(c))  # Output: 10001 <class 'str'>

if __name__ == "__main__":
    main()
```

### 4. Negative Binary

```python
def main():
    a = -17
    b = bin(a)
    print(b, type(b))  # Output: -0b10001 <class 'str'>

if __name__ == "__main__":
    main()
```

### 5. Binary to Decimal

```python
def main():
    a = 0b10001
    b = int(a)
    print(b, type(b))  # Output: 17 <class 'int'>

    a = 0B10001
    b = int(a)
    print(b, type(b))  # Output: 17 <class 'int'>

    a = "0b10001"
    b = int(a[2:], 2)
    print(b, type(b))  # Output: 17 <class 'int'>

    a = "0B10001"
    b = int(a[2:], 2)
    print(b, type(b))  # Output: 17 <class 'int'>

if __name__ == "__main__":
    main()
```

### 6. Negative Conversion

```python
def main():
    a = -0b10001
    b = int(a)
    print(b, type(b))  # Output: -17 <class 'int'>

    a = -0B10001
    b = int(a)
    print(b, type(b))  # Output: -17 <class 'int'>

    a = "-0b10001"
    b = -int(a[3:], 2)
    print(b, type(b))  # Output: -17 <class 'int'>

    a = "-0B10001"
    b = -int(a[3:], 2)
    print(b, type(b))  # Output: -17 <class 'int'>

if __name__ == "__main__":
    main()
```

---

## Octal

Octal representation uses base 8 with prefix `0o` or `0O`.

### 1. Octal Literals

```python
def main():
    a = 0o10
    print(a, type(a))
    print(f"{a = }")
    print(f"{a = :d}") # Decimal Representation
    print(f"{a = :b}") # Binary Representation
    print(f"{a = :o}") # Octal Representation
    print(f"{a = :x}") # Hexadecimal Representation

if __name__ == "__main__":
    main()
```

### 2. Capital Prefix

```python
def main():
    a = 0O10
    print(a, type(a))
    print(f"{a = }")
    print(f"{a = :d}") # Decimal Representation
    print(f"{a = :b}") # Binary Representation
    print(f"{a = :o}") # Octal Representation
    print(f"{a = :x}") # Hexadecimal Representation

if __name__ == "__main__":
    main()
```

### 3. Decimal to Octal

```python
def main():
    a = 17
    b = oct(17)
    print(b, type(b))  # Output: 0o21 <class 'str'>

if __name__ == "__main__":
    main()
```

### 4. Negative Octal

```python
def main():
    a = -17
    b = oct(17)
    print(b, type(b))  # Output: 0o21 <class 'str'>

if __name__ == "__main__":
    main()
```

### 5. Octal to Decimal

```python
def main():
    a = 0o21
    b = int(a)
    print(b, type(b))  # Output: 17 <class 'int'>

    a = 0O21
    b = int(a)
    print(b, type(b))  # Output: 17 <class 'int'>

    a = "0o21"
    b = int(a[2:], 8)
    print(b, type(b))  # Output: 17 <class 'int'>

    a = "0O21"
    b = int(a[2:], 8)
    print(b, type(b))  # Output: 17 <class 'int'>

if __name__ == "__main__":
    main()
```

### 6. Negative Conversion

```python
def main():
    a = -0o21
    b = int(a)
    print(b, type(b))  # Output: -17 <class 'int'>

    a = -0O21
    b = int(a)
    print(b, type(b))  # Output: -17 <class 'int'>

    a = "-0o21"
    b = -int(a[3:], 8)
    print(b, type(b))  # Output: -17 <class 'int'>

    a = "-0O21"
    b = -int(a[3:], 8)
    print(b, type(b))  # Output: -17 <class 'int'>

if __name__ == "__main__":
    main()
```

---

## Hexadecimal

Hexadecimal representation uses base 16 with prefix `0x` or `0X`.

### 1. Hex Literals

```python
def main():
    a = 0x1f
    print(a, type(a))
    print(f"{a = }")
    print(f"{a = :d}") # Decimal Representation
    print(f"{a = :b}") # Binary Representation
    print(f"{a = :o}") # Octal Representation
    print(f"{a = :x}") # Hexadecimal Representation

if __name__ == "__main__":
    main()
```

### 2. Capital Prefix

```python
def main():
    a = 0X1f
    print(a, type(a))
    print(f"{a = }")
    print(f"{a = :d}") # Decimal Representation
    print(f"{a = :b}") # Binary Representation
    print(f"{a = :o}") # Octal Representation
    print(f"{a = :x}") # Hexadecimal Representation

if __name__ == "__main__":
    main()
```

### 3. Decimal to Hex

```python
def main():
    a = 1117
    b = hex(a)
    print(b, type(b))  # Output: 0x45d <class 'str'>

if __name__ == "__main__":
    main()
```

### 4. Negative Hex

```python
def main():
    a = -17
    b = hex(a)
    print(b, type(b))  # Output: -0x11 <class 'str'>

if __name__ == "__main__":
    main()
```

### 5. Hex to Decimal

```python
def main():
    a = 0x11
    b = int(a)
    print(b, type(b))  # Output: 17 <class 'int'>

    a = 0X11
    b = int(a)
    print(b, type(b))  # Output: 17 <class 'int'>

    a = "0x11"
    b = int(a[2:],16)
    print(b, type(b))  # Output: 17 <class 'int'>

    a = "0X11"
    b = int(a[2:],16)
    print(b, type(b))  # Output: 17 <class 'int'>

if __name__ == "__main__":
    main()
```

### 6. Negative Conversion

```python
def main():
    a = -0x11
    b = int(a)
    print(b, type(b))  # Output: -17 <class 'int'>

    a = -0X11
    b = int(a)
    print(b, type(b))  # Output: -17 <class 'int'>

    a = "-0x11"
    b = -int(a[3:],16)
    print(b, type(b))  # Output: -17 <class 'int'>

    a = "-0X11"
    b = -int(a[3:],16)
    print(b, type(b))  # Output: -17 <class 'int'>

if __name__ == "__main__":
    main()
```

---

## Conclusion

Python's support for multiple number systems makes it easy to work with different bases. Understanding these representations is essential for low-level programming, bit manipulation, and working with hardware interfaces.
