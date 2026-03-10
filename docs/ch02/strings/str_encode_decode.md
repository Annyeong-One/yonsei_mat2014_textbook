# `str`: Encode and Decode


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

Python provides methods to convert between strings and bytes using various encodings.

---

## Basic Methods

### 1. The `encode()` Method

Convert a string to bytes:

```python
s = "Hello, 世界"
encoded = s.encode('utf-8')
print(encoded)        # b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(type(encoded))  # <class 'bytes'>
```

### 2. The `decode()` Method

Convert bytes back to a string:

```python
encoded = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
decoded = encoded.decode('utf-8')
print(decoded)        # Hello, 世界
print(type(decoded))  # <class 'str'>
```

---

## Encoding Diagram

$$\begin{array}{ccccc}
&\text{Encoding}&&\text{Decoding}\\
\text{"Hi"}&\longrightarrow&\text{b"Hi"}&\longrightarrow&\text{"Hi"}\\
&\text{encode}&&\text{decode}\\
\end{array}$$

---

## Bytes Object

### 1. Understanding Output

The `b` prefix indicates a bytes object:

```python
s = "Hello, 世界"
encoded = s.encode('utf-8')
print(encoded)  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
```

Breaking down the output:

- `Hello, ` → ASCII characters (1 byte each)
- `\xe4\xb8\x96` → '世' encoded as 3 bytes
- `\xe7\x95\x8c` → '界' encoded as 3 bytes

### 2. Iterating Bytes

Bytes iterate as integers:

```python
def print_encode_decode(words):
    a = words
    aa = a.encode()
    aaa = aa.decode()

    print(f"{a   = },  {type(a) = }")
    print(f"{aa  = }, {type(aa) = }")
    print(f"{aaa = },  {type(aaa) = }")
    print("-" * 50)

    for i in a:
        print(i, type(i), end=" | ")
    print()
    for i in aa:
        print(i, type(i), end=" | ")
    print()

def main():
    words = "Hi"
    print_encode_decode(words)

if __name__ == "__main__":
    main()
```

---

## Language Examples

### 1. English

```python
def main():
    words = "Hi"
    print(words.encode())  # b'Hi'

if __name__ == "__main__":
    main()
```

### 2. Hebrew

```python
def main():
    words = "היי"
    print(words.encode())  # b'\xd7\x94\xd7\x99\xd7\x99'

if __name__ == "__main__":
    main()
```

### 3. Japanese

```python
def main():
    words = "こんにちは"
    print(words.encode())
    # b'\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf'

if __name__ == "__main__":
    main()
```

### 4. Chinese

```python
def main():
    words = "你好"
    print(words.encode())  # b'\xe4\xbd\xa0\xe5\xa5\xbd'

if __name__ == "__main__":
    main()
```

### 5. Korean

```python
def main():
    words = "안녕"
    print(words.encode())  # b'\xec\x95\x88\xeb\x85\x95'

if __name__ == "__main__":
    main()
```

---

## Byte Breakdown

### 1. Chinese Example

For `"Hello, 世界"`:

| Character | Code Point | UTF-8 Bytes |
|-----------|------------|-------------|
| H | U+0048 | `0x48` |
| e | U+0065 | `0x65` |
| l | U+006C | `0x6c` |
| l | U+006C | `0x6c` |
| o | U+006F | `0x6f` |
| , | U+002C | `0x2c` |
| (space) | U+0020 | `0x20` |
| 世 | U+4E16 | `\xe4\xb8\x96` |
| 界 | U+754C | `\xe7\x95\x8c` |

### 2. Why 3 Bytes?

Chinese characters fall in range U+0800–U+FFFF, requiring 3 UTF-8 bytes:

```
世 (U+4E16):
Binary: 0100 1110 0001 0110
UTF-8:  1110 0100 | 1011 1000 | 1001 0110
Hex:       \xe4       \xb8       \x96
```

---

## Key Takeaways

- `encode()` converts str to bytes.
- `decode()` converts bytes to str.
- UTF-8 is the default encoding.
- Bytes display as hex for non-ASCII.
