# Character Encoding Preview

## The Problem: Characters Are Not Numbers

Computers store bits. Character encoding defines how sequences of bits represent characters — it is the agreed-upon convention between character and number.

```
'A' → 65 → 0100 0001
 ↑     ↑       ↑
char  number  bits

This mapping is a convention agreed upon by standards bodies.
Many assignments follow design constraints: digits are contiguous
(48–57), uppercase letters contiguous (65–90), lowercase contiguous
(97–122) — which is why ord('a') - ord('A') = 32 always holds.
```

## ASCII: The Foundation

**ASCII** (American Standard Code for Information Interchange) was the original standard, defining 128 characters using 7 bits. In practice, ASCII characters are always stored in 8-bit bytes — the high bit is zero, leaving room for the extended encodings that came later:

```
ASCII Table (partial)
┌─────────┬────────┬─────────────────────────┐
│ Decimal │  Char  │      Description        │
├─────────┼────────┼─────────────────────────┤
│  0-31   │ (ctrl) │ Control characters      │
│  32     │ (space)│ Space                   │
│  48-57  │ 0-9    │ Digits                  │
│  65-90  │ A-Z    │ Uppercase letters       │
│  97-122 │ a-z    │ Lowercase letters       │
│  127    │ (del)  │ Delete                  │
└─────────┴────────┴─────────────────────────┘
```

### ASCII in Python

```python
# Character to code
print(ord('A'))  # 65
print(ord('a'))  # 97
print(ord('0'))  # 48

# Code to character
print(chr(65))   # 'A'
print(chr(97))   # 'a'
print(chr(48))   # '0'

# ASCII relationships
print(ord('B') - ord('A'))  # 1
print(ord('a') - ord('A'))  # 32 (lowercase offset)
```

### ASCII Limitations

ASCII only covers English:

- No accented characters (é, ñ, ü)
- No non-Latin scripts (中文, العربية, 한글)
- No emoji (😀)
- Only 128 characters total

## Incompatible 8-bit Encodings

Many incompatible 8-bit encodings extended ASCII by using the high bit (values 128–255) for additional characters. There is no single "Extended ASCII" standard — each encoding made different choices:

```
Latin-1 (ISO-8859-1): Western European
Latin-2 (ISO-8859-2): Central European
Windows-1252: Microsoft's Western European
```

**Problem**: The same byte could mean different characters in different encodings!

```
Byte 0xE9:
  Latin-1:      é
  Latin-2:      é
  Windows-1252: é
  Greek (1253): ι
```

## Unicode: Universal Character Set

**Unicode** assigns a unique number (code point) to every character in every language. It is important to distinguish:

- **Unicode** — a *character set*: defines which characters exist and their code points
- **UTF-8 / UTF-16 / UTF-32** — *encodings*: define how those code points are stored as bytes

This distinction matters: you can have a Unicode code point without knowing how it is encoded into bytes.

```
Unicode Code Points (examples)
┌────────────┬───────┬──────────────────────┐
│ Code Point │ Char  │    Description       │
├────────────┼───────┼──────────────────────┤
│ U+0041     │ A     │ Latin Capital A      │
│ U+00E9     │ é     │ Latin Small E Acute  │
│ U+4E2D     │ 中    │ CJK for "middle"     │
│ U+1F600    │ 😀    │ Grinning Face        │
│ U+1F9D1    │ 🧑    │ Person               │
└────────────┴───────┴──────────────────────┘
```

### Unicode in Python

```python
# Unicode escapes
print('\u0041')      # A
print('\u00e9')      # é
print('\u4e2d')      # 中
print('\U0001F600')  # 😀 (note: uppercase U for >4 hex digits)

# Get code point
print(hex(ord('中')))  # '0x4e2d'
print(hex(ord('😀')))  # '0x1f600'

# Python strings are sequences of Unicode code points
text = "Hello, 世界! 🌍"
print(len(text))  # 12 (code points, not bytes)
# Note: len() counts code points, not user-perceived characters.
# Some visible characters are composed of multiple code points
# (e.g. é can be e + combining accent = 2 code points but looks like 1).
# See the full chapter for grapheme clusters.
```

## UTF-8: The Dominant Encoding

**UTF-8** is a variable-width encoding for Unicode:

```
UTF-8 Encoding Scheme
┌──────────────────┬───────────────────────────────────────┐
│ Code Point Range │           UTF-8 Bytes                 │
├──────────────────┼───────────────────────────────────────┤
│ U+0000 - U+007F  │ 0xxxxxxx (1 byte, ASCII compatible)   │
│ U+0080 - U+07FF  │ 110xxxxx 10xxxxxx (2 bytes)           │
│ U+0800 - U+FFFF  │ 1110xxxx 10xxxxxx 10xxxxxx (3 bytes)  │
│ U+10000 - U+10FFFF│ 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx   │
└──────────────────┴───────────────────────────────────────┘
```

The leading bits of the first byte tell you how many bytes follow: `0` means 1 byte, `110` means 2, `1110` means 3, `11110` means 4. All **continuation bytes** start with `10xxxxxx` — this pattern never appears as a leading byte, which is what makes UTF-8 **self-synchronizing**: given any byte in a stream, you can immediately tell whether it is a leading byte or a continuation byte, so you can find character boundaries without scanning from the start.

### UTF-8 Examples

```python
# ASCII characters: 1 byte (UTF-8 is backward-compatible with ASCII)
'A'.encode('utf-8')   # b'A'           — 1 byte: 0x41 = 65

# Accented Latin: 2 bytes
'é'.encode('utf-8')   # b'\xc3\xa9'   — 2 bytes: U+00E9

# CJK (Chinese/Japanese/Korean): 3 bytes
'中'.encode('utf-8')  # b'\xe4\xb8\xad' — 3 bytes: U+4E2D

# Emoji: 4 bytes (outside the Basic Multilingual Plane)
'😀'.encode('utf-8')  # b'\xf0\x9f\x98\x80' — 4 bytes: U+1F600
```

### Why UTF-8 Dominates

1. **ASCII compatible**: First 128 characters are identical
2. **Compact for English**: No wasted bytes for ASCII text
3. **Self-synchronizing**: Can find character boundaries in any position
4. **No byte-order issues**: Unlike UTF-16/32

## Encoding and Decoding in Python

### String ↔ Bytes

```python
# Encode: str → bytes
# .encode() converts Unicode characters into raw bytes using the given encoding rule
text = "Hello, 世界!"
encoded = text.encode('utf-8')
print(encoded)        # b'Hello, \xe4\xb8\x96\xe7\x95\x8c!'
                      # b'...' prefix: this is a bytes object (sequence of 8-bit bytes)
                      # ASCII chars shown as-is; non-ASCII shown as hex escapes (\xNN)
print(len(text))      # 10  — number of Unicode characters
print(len(encoded))   # 14  — number of bytes (世 = 3 bytes, 界 = 3 bytes in UTF-8)

# Decode: bytes → str
# .decode() reverses the process: raw bytes → Unicode string using the same encoding rule
decoded = encoded.decode('utf-8')
print(decoded)        # Hello, 世界!
```

### Handling Encoding Errors

```python
# Invalid UTF-8 bytes
invalid = b'\xff\xfe'

# Default: raises exception
try:
    invalid.decode('utf-8')
except UnicodeDecodeError as e:
    print(f"Error: {e}")

# Alternative error handlers
print(invalid.decode('utf-8', errors='replace'))  # ��
print(invalid.decode('utf-8', errors='ignore'))   # (empty)
print(invalid.decode('utf-8', errors='backslashreplace'))  # \xff\xfe
```

### File Encoding

```python
# Always specify encoding for text files
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, 世界!')

with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Detect system default
import locale
print(locale.getpreferredencoding())  # e.g., 'UTF-8'
```

## Common Encodings

| Encoding | Bytes per Code Point | Use Case |
|----------|---------------------|----------|
| ASCII | 1 | English only, legacy |
| UTF-8 | 1-4 | Web, Linux, general |
| UTF-16 | 2-4 | Windows internal, Java |
| UTF-32 | 4 | Fixed width, processing |
| Latin-1 | 1 | Western European legacy |

## Code Point vs Byte Length

```python
import sys

text = "Hello"
print(len(text))               # 5  — 5 code points
print(len(text.encode('utf-8')))  # 5  — 5 bytes (ASCII: 1 byte per code point)

text = "世界"
print(len(text))               # 2  — 2 code points
print(len(text.encode('utf-8')))  # 6  — 6 bytes (CJK: 3 bytes per code point)

text = "😀😀"
print(len(text))               # 2  — 2 code points
print(len(text.encode('utf-8')))  # 8  — 8 bytes (emoji: 4 bytes per code point)
```

## NumPy and Strings

```python
import numpy as np

# NumPy stores Unicode strings as fixed-width UTF-32 internally
# (4 bytes per code point), regardless of the actual characters used
arr = np.array(['hello', 'world', '世界'])
print(arr.dtype)  # '<U5' (Unicode, max 5 code points, 4 bytes each = 20 bytes per element)

# Bytes
arr_bytes = np.array([b'hello', b'world'])
print(arr_bytes.dtype)  # '|S5' (byte string, 5 bytes)

# Memory usage differs significantly
unicode_arr = np.array(['a'] * 1000)  # 4 bytes per code point (UTF-32 internally)
byte_arr = np.array([b'a'] * 1000)    # 1 byte per element
```

## Common Pitfalls

### Mojibake (Garbled Text)

```python
# Text encoded one way, decoded another
text = "café"
wrong = text.encode('utf-8').decode('latin-1')
print(wrong)  # cafÃ© (mojibake!)

# Fix: use correct encoding
right = text.encode('utf-8').decode('utf-8')
print(right)  # café
```

### BOM (Byte Order Mark)

```python
# Some files start with BOM
bom_utf8 = b'\xef\xbb\xbf'  # UTF-8 BOM

# Read with BOM handling
with open('file.txt', 'r', encoding='utf-8-sig') as f:
    content = f.read()  # BOM automatically stripped
```

## Summary

| Concept | Description |
|---------|-------------|
| **ASCII** | 7-bit encoding for English (128 chars) |
| **Unicode** | Universal character set (1.1M+ code points) |
| **UTF-8** | Variable-width Unicode encoding (1-4 bytes) |
| **Code Point** | Number assigned to a character (U+XXXX) |
| **Encoding** | str → bytes |
| **Decoding** | bytes → str |

Key points:

- Always know your encoding (especially for files)
- UTF-8 is the default choice for most purposes
- Unicode is a character set; UTF-8/16/32 are encodings of that character set
- Code point length ≠ byte length for non-ASCII text
- `len()` counts Unicode code points, not user-perceived characters (grapheme clusters)
- Use `encoding='utf-8'` explicitly in file operations
- Python 3 strings are sequences of Unicode code points; bytes are raw data

This is a preview—see Chapter 2 (str ASCII and Unicode, str UTF-8 Encoding) for complete details.
