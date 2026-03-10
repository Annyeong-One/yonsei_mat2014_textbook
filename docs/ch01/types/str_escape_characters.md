# `str`: Escape Characters


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Escape characters allow representing special characters within strings using backslash notation.

---

## Common Escapes

### 1. Tab and Newline

The most frequently used escape sequences:

```python
def main():
    a = 1
    b = "Hello"
    c = "world"
    
    # Tab separator
    print(a, b, c, sep="\t")  # 1    Hello    world
    
    # Newline separator
    print(a, b, c, sep="\n")
    # 1
    # Hello
    # world

if __name__ == "__main__":
    main()
```

### 2. Quote Escapes

Escape quotes within strings:

```python
def main():
    # Single quote escape
    a = 'Bob\'s hat'
    print(a)  # Bob's hat
    
    # Double quote escape
    a = "He said \"Hello\""
    print(a)  # He said "Hello"

if __name__ == "__main__":
    main()
```

### 3. Backslash Escape

Escape the backslash itself:

```python
path = "C:\\Users\\Documents"
print(path)  # C:\Users\Documents
```

---

## Reference Table

| Escape | Meaning |
|--------|---------|
| `\t` | Tab |
| `\n` | Newline |
| `\'` | Single quote |
| `\"` | Double quote |
| `\\` | Backslash |
| `\b` | Backspace |

### 1. Backspace Example

```python
def main():
    a = 'Bob\b\bOB'
    print(a)  # BOB (backspace removes 'o' and 'b')

if __name__ == "__main__":
    main()
```

---

## Numeric Escapes

### 1. Octal Notation

The `\ooo` notation uses octal (base-8) ASCII values:

```python
def main():
    # Octal: 145=e, 154=l, 157=o
    a = 'H\145\154\154\157'
    print(a)  # Hello
    
    # Full word in octal
    a = '\110\145\154\154\157'
    print(a)  # Hello

if __name__ == "__main__":
    main()
```

### 2. Hexadecimal Notation

The `\xhh` notation uses hexadecimal (base-16) ASCII values:

```python
def main():
    # Hex: 65=e, 6c=l, 6f=o
    a = 'H\x65\x6c\x6c\x6f'
    print(a)  # Hello
    
    # Full word in hex
    a = '\x48\x65\x6c\x6c\x6f'
    print(a)  # Hello

if __name__ == "__main__":
    main()
```

---

## Key Takeaways

- Backslash (`\`) initiates escape sequences.
- Common escapes: `\t`, `\n`, `\'`, `\"`, `\\`.
- Octal (`\ooo`) and hex (`\xhh`) encode ASCII values.
