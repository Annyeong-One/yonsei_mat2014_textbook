# `str`: Encode and Decode

Python converts between text (`str`) and binary data (`bytes`) using `encode()` and `decode()`.

| Type    | Meaning         |
| ------- | --------------- |
| `str`   | Unicode text    |
| `bytes` | raw binary data |

Text must be **encoded into bytes** before it can be written to files, sent over networks, or stored in binary formats.

---

## Text and Bytes Model

Encoding converts text into bytes, and decoding converts bytes back into text.

```
str (Unicode text)
      ↓ encode()
bytes (UTF-8 or other encoding)
      ↓ decode()
str (Unicode text)
```

Example:

```python
def main():
    text = "Hello, 世界"

    data = text.encode("utf-8")     # text → bytes
    decoded = data.decode("utf-8")  # bytes → text

    print(text)
    print(data)
    print(decoded)

if __name__ == "__main__":
    main()
```

Output:

```
Hello, 世界
b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
Hello, 世界
```

---

## The `encode()` Method

`encode()` converts a **string (`str`) into bytes**.

```python
def main():
    text = "Hello, 世界"

    encoded = text.encode("utf-8")

    print(encoded)
    print(type(encoded))

if __name__ == "__main__":
    main()
```

Output:

```
b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
<class 'bytes'>
```

---

## The `decode()` Method

`decode()` converts **bytes back into text**.

```python
def main():
    data = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'

    decoded = data.decode("utf-8")

    print(decoded)
    print(type(decoded))

if __name__ == "__main__":
    main()
```

Output:

```
Hello, 世界
<class 'str'>
```

---

## Byte Breakdown Example

Consider the string:

```python
text = "Hello, 世界"
```

| Character | Code Point | UTF-8 Bytes    |
| --------- | ---------- | -------------- |
| H         | U+0048     | `0x48`         |
| e         | U+0065     | `0x65`         |
| l         | U+006C     | `0x6c`         |
| l         | U+006C     | `0x6c`         |
| o         | U+006F     | `0x6f`         |
| ,         | U+002C     | `0x2c`         |
| space     | U+0020     | `0x20`         |
| 世         | U+4E16     | `\xe4\xb8\x96` |
| 界         | U+754C     | `\xe7\x95\x8c` |

ASCII characters use **1 byte**, while Chinese characters use **3 bytes** in UTF-8. As explained in the UTF-8 chapter, characters in the range U+0800–U+FFFF require three bytes in UTF-8.

Example encoding:

```
世 (U+4E16)
Binary: 0100111000010110
UTF-8:  11100100 10111000 10010110
Hex:    \xe4 \xb8 \x96
```

---

## Iterating Over `str` vs `bytes`

Strings iterate over **characters**, but bytes iterate over **integers**.

```python
def main():
    text = "Hi"
    encoded = text.encode("utf-8")

    print("Iterating str:")
    for c in text:
        print(c, type(c))

    print("\nIterating bytes:")
    for b in encoded:
        print(b, type(b))

if __name__ == "__main__":
    main()
```

Output:

```
Iterating str:
H <class 'str'>
i <class 'str'>

Iterating bytes:
72 <class 'int'>
105 <class 'int'>
```

| Object  | Iteration result |
| ------- | ---------------- |
| `str`   | characters       |
| `bytes` | integers         |

---

## Multilingual Encoding Examples

Encoding works the same way for all languages.

```python
def main():
    print("Hi".encode())
    print("你好".encode())
    print("こんにちは".encode())

if __name__ == "__main__":
    main()
```

Example output:

```
b'Hi'
b'\xe4\xbd\xa0\xe5\xa5\xbd'
b'\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf'
```

UTF-8 can encode **every writing system**.

---

## Common Encoding Errors in Python

When working with text and bytes, incorrect encoding assumptions can cause errors.

| Error                | Meaning                                                    |
| -------------------- | ---------------------------------------------------------- |
| `UnicodeEncodeError` | Python cannot convert text into the requested encoding     |
| `UnicodeDecodeError` | Python cannot interpret bytes using the specified encoding |

---

### `UnicodeEncodeError`

This occurs when a character **cannot be represented in the target encoding**.

```python
text = "你好"

text.encode("ascii")
```

Error:

```
UnicodeEncodeError: 'ascii' codec can't encode characters
```

ASCII supports only characters in the range U+0000 – U+007F. Chinese characters fall outside this range.

Correct solution:

```python
text.encode("utf-8")
```

---

### `UnicodeDecodeError`

This occurs when bytes are decoded using the **wrong encoding**.

```python
data = "你好".encode("utf-8")

data.decode("ascii")
```

Error:

```
UnicodeDecodeError: 'ascii' codec can't decode byte
```

This happens because the byte sequence was encoded with **UTF-8**, not ASCII.

Correct solution:

```python
data.decode("utf-8")
```

---

### Handling Encoding Errors

Python allows you to control how encoding errors are handled.

```python
def main():
    text = "你好"

    print(text.encode("ascii", errors="ignore"))
    print(text.encode("ascii", errors="replace"))

if __name__ == "__main__":
    main()
```

Output:

```
b''
b'??'
```

Common error handlers:

| Option      | Behavior                     |
| ----------- | ---------------------------- |
| `"strict"`  | raise an exception (default) |
| `"ignore"`  | skip invalid characters      |
| `"replace"` | replace with `?`             |

Most encoding errors occur because **the wrong encoding is assumed**. Always ensure that the encoding used for `decode()` matches the encoding used for `encode()`.

---

## Key Takeaways

* `str` represents **Unicode text**.
* `bytes` represents **binary data**.
* `encode()` converts **text → bytes**.
* `decode()` converts **bytes → text**.
* UTF-8 is the **default encoding in Python 3**.
* ASCII characters use **1 byte**, while many Unicode characters use **multiple bytes**.
* Encoding mismatches cause `UnicodeEncodeError` and `UnicodeDecodeError`.
